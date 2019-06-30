from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SubmitField,BooleanField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Kindly enter your email address',validators=[Required(),Email()])
    username = StringField('Kindly enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('Sorry, an account is already registered with that email address')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Sorry, that username is already taken')


class LoginForm(FlaskForm):
    email = StringField('Kindly Enter Your Email Address Here',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login In')
