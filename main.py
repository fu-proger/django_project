import datetime

from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
@app.route('/index') # alksfhlakfhslkaa
def index():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    req_jobs = db_sess.query(Jobs).all()
    return render_template('index.html', jobs=req_jobs)


def main():
    app.run(host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()