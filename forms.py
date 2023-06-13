from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class RegistrateForm(FlaskForm):
    name = StringField('Username: ', validators=[DataRequired(message='Please enter your first name'), Length(min=6, max=50)])
    surname = StringField('Username: ', validators=[DataRequired(message='Please enter your last name'), Length(min=6, max=50)])
    email = StringField('Email: ', validators=[Email(message='Please enter your email'), Length(min=4, max=100)])
    password = PasswordField('Password: ', validators=[DataRequired(message='Please enter your password'), Length(min=8, max=255)])
    passconf = PasswordField('Password Again: ', validators=[DataRequired(message='Enter the password again'), Length(min=8, max=255)])
    submit = SubmitField('Authorized')


class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[Email(message='Not a valid email address'), DataRequired('Please enter your e-mail')])
    password = PasswordField('Password: ', validators=[DataRequired(message='Please enter your password'), Length(min=6, max=100)])
    submit = SubmitField('LogIn')

class ContactForm(FlaskForm):
    name = StringField('Name : ', validators=[DataRequired(message='Please enter your name'), Length(min=2, max=50)])
    email = StringField('e-mail : ', validators=[Email(message='Not a valid email address')])
    subject = StringField('subject : ', validators=[DataRequired(message='Please enter a subject'), Length(min=2, max=1023)])
    message = TextAreaField('Text : ', validators=[DataRequired(message='Please enter your massege'), Length(min=3, max=1024)])
    submit = SubmitField('Send Message')

class SearchForm(FlaskForm):
    word = StringField('Enter word : ', validators=[DataRequired('Please enter search word'), Length(min=2, max=255)])

class ReviewForm(FlaskForm):
    review = StringField('Enter text : ', validators=[DataRequired('Please enter a review'), Length(min=3, max=1024)])

