from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, StringField, IntegerField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired


class AddJob(FlaskForm):
    team_leader = IntegerField('Тимлид', validators=[DataRequired()])
    job = StringField('Работа', validators=[DataRequired()])
    work_size = StringField('Продолжительность', validators=[DataRequired()])
    collaborators = StringField('Партнёры', validators=[DataRequired()])
    is_finished = BooleanField('РОбота окончена?')
    submit = SubmitField('Сохранить')