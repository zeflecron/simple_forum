from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField,
                     TextAreaField, SelectField)
from wtforms.validators import (DataRequired, Length, Email, EqualTo,
                                ValidationError)
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'Username already exists, login or choose another one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'Email already exists, login or choose another one')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    image = FileField('Update Profile Picture',
                      validators=[FileAllowed(['png', 'jpg'])])
    description = StringField('Description',
                              validators=[Length(min=0, max=80)])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'Username already exists, login or choose another one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'Email already exists, login or choose another one')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('General', 'General'),
        ('Programming', 'Programming'),
        ('Computer Hardware', 'Computer Hardware'),
        ('Operating System', 'Operating System'),
        ('Computer Network', 'Computer Network'),
        ('Computer Security', 'Computer Security'),
    ])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')
