
from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,SubmitField,SelectField,PasswordField
from wtforms import validators
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired,Length




class CreditForm(FlaskForm):
	amount=IntegerField('amount',validators=[DataRequired()])
	transaction_type=SelectField('transaction_type',choices=['Credit','Debit'],validators=[DataRequired()])
	Transaction_by=StringField('Transaction_by',validators=[DataRequired(),Length(max=15)])
	purpose=SelectField('purpose',choices=['food','rent','fuel'],validators=[DataRequired()])
	form_of_transaction=SelectField("form_of_transaction",choices=['cash','card'],validators=[DataRequired()])
	submit=SubmitField('submit')


class RegisterForm(FlaskForm):
	username=StringField('username',validators=[DataRequired()])
	email=StringField('email',validators=[DataRequired()])
	password=PasswordField('password',validators=[DataRequired()])
	confirm_password=PasswordField('confirm_password',validators=[DataRequired()])
	submit=SubmitField("submit")

class LoginForm(FlaskForm):
	email=StringField('email',validators=[DataRequired()])
	password=PasswordField('password',validators=[DataRequired()])
	submit=SubmitField("submit")