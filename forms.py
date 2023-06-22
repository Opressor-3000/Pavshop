from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField, SearchField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, Length, ValidationError,EqualTo
from models import User


class RegistrateForm(FlaskForm):
    name = StringField('Username: ', validators=[DataRequired(message='Please enter your first name'), Length(min=2, max=50, message="The NAME must be between 2 and 50 characters")])
    surname = StringField('Username: ', validators=[DataRequired(message='Please enter your last name'), Length(min=2, max=50, message='The SURNAME must be between 2 and 50 character')])
    e_mail = StringField('Email: ', validators=[Email(message='Wrong email format')])
    password = PasswordField('Password: ', validators=[DataRequired(message='Please enter your password'), Length(min=8, max=255, message="The password length must be between 8 and 255 characters")])
    passconf = PasswordField('Password Again: ', validators=[DataRequired(message='Enter the password again'), EqualTo('password', message="Password does not match")])
    # submit = SubmitField('SignUp')

    def vld_email(self, e_mail):
        exemail = User.query.filter_by(email=e_mail.data).first()
        if exemail:
            raise ValidationError('This email its used, please enter another email')
        else:
            True


class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[Email(message='Not a valid email address')])
    password = PasswordField('Password: ', validators=[DataRequired(message='Please enter your password'), Length(min=6, max=100, message="Wrong password")])
    rememb = BooleanField('Remember me: ', default=False)
    submit = SubmitField('LogIn')

class ContactForm(FlaskForm):
    subject = StringField('subject : ', validators=[DataRequired(message='Please enter a subject'), Length(min=2, max=100)])
    message = TextAreaField('Text : ', validators=[DataRequired(message='Please enter your massege'), Length(min=3, max=1023, message='The MESSAGE must be between 3 and 1023 characters')])
    submit = SubmitField('Send Message')

class SearchForm(FlaskForm):
    word = SearchField('Enter word : ', validators=[DataRequired('Please enter search word'), Length(min=2, max=100, message='The Search word must be between 2 and 255 characters')])

class ReviewForm(FlaskForm):
    review = TextAreaField('Enter text : ', validators=[DataRequired('Please enter a review'), Length(min=3, max=1024, message='The Review must be between 3 and 50 characte')])
    submit = SubmitField('Leave Your Review')


class ItemForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    price = FloatField(validators=[DataRequired()])
    oldprice = FloatField(validators=[DataRequired()])
    image = StringField(validators=[DataRequired()])
    quantity = IntegerField(validators=[DataRequired()])
    category = IntegerField(validators=[Length(min=1, max=2)])
    description = TextAreaField(validators=[Length(min=3, max=1024)])
    submit = SubmitField('add item')

class FavoriteForm(FlaskForm):
    favadd = SubmitField('Add to Favorite')

    # <img class="img-fluid w-100" src="../static/img/pr-1.webp" alt="" />