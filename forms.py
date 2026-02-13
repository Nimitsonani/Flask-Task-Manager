from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LogIn(FlaskForm):
    email = StringField(label="Email: ", validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    login = SubmitField('Log In')

class SignUp(FlaskForm):
    name = StringField(label="Name: ", validators=[DataRequired()])
    email = StringField(label="Email: ", validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    signup = SubmitField('Sign Up')

class TaskForm(FlaskForm):
    task = StringField("", validators=[DataRequired()], render_kw={"placeholder": "Add a new task..."})
    add = SubmitField('Add')