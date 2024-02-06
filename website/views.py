from flask import Blueprint ,render_template
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from wtforms import TelField, SubmitField
from wtforms.validators import DataRequired

views = Blueprint('views',__name__)

@views.route('/')
def welcome():
    return render_template('welcome.html', user=current_user)

@views.route('/account')
def account():
    return render_template('account.html', user=current_user)

@views.route('/article')
def article():
    return render_template('article.html', user=current_user)

@views.route('/Categories')
def Categories():
    return render_template('Categories.html', user=current_user)

@views.route('/normal')
def normal():
    return render_template('normal.html', user=current_user)

@views.route('/obese')
def obese():
    return render_template('obese.html', user=current_user)

@views.route('/overweight')
def overweight():
    return render_template('overweight.html', user=current_user)

@views.route('/underweight')
def underweight():
    return render_template('underweight.html', user=current_user)









class MyForm(FlaskForm):
    # Define TelFields for height and weight, and a SubmitField
    height = TelField('Enter your height (m)', validators=[DataRequired()])
    weight = TelField('Enter your weight (Kg)', validators=[DataRequired()])
    submit = SubmitField('Submit')
    save_submit = SubmitField('Save and Submit')

# Define a route for '/bmi' with support for both GET and POST methods
@views.route('/bmi', methods=['GET', 'POST'])
@login_required
def bmi():
    # Initialize variables and create a MyForm instance
    height = weight = Categories = bmi_value = None
    Form = MyForm()
    return render_template('bmi.html', form=Form, weight=weight, height=height, bmi=bmi_value, Categories=Categories, user=current_user)

