from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class LoginForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class SignupForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password',
                           validators=
                            [DataRequired(),
                             Length(min=6,
                                    message='Please select a stronger password.')])
    confirm = PasswordField('Confirm your Password',
                           validators=[DataRequired(),
                                       EqualTo('password',
                                                message='Passwords must match.')])
    submit = SubmitField('Register')
