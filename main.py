import datetime

from flask import Flask, render_template, request, make_response, session, redirect
from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired
from data import db_session
from data.users import User
from data.jobs import Jobs
from flask_login import LoginManager, login_user
from data.login_form import LoginForm
from data.add_job_form import AddJob


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    form = AddJob()
    if form.validate_on_submit():
        db_session.global_init("db/mars_explorer.db")
        db_sess = db_session.create_session()

        jobs = Jobs(
            job=form.job.data,
            team_leader=form.team_leader.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data
        )
        db_sess.add(jobs)
        db_sess.commit()
    return render_template('add_job.html', title='Авторизация', form=form)

@app.route('/')
@app.route('/index')
def index():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    req_jobs = db_sess.query(Jobs).all()
    return render_template('index.html', jobs=req_jobs)

def main():
    app.run(host='127.0.0.1', port=5000)

    # db_session.global_init("db/mars_explorer.db")
    # db_sess = db_session.create_session()

    # user = User()
    # user.surname = "Bass"
    # user.name = "Lika"
    # user.age = 10
    # user.position = "captain3"
    # user.speciality = "caption3"
    # user.address = "module_1"
    # user.email = "bass_lika@mars.org"
    # user.set_password("12345678")
    #
    # db_sess.add(user)
    # db_sess.commit()


if __name__ == '__main__':
    main()
