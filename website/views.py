from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from wtforms import TelField, SubmitField
from wtforms.validators import DataRequired
import datetime
from . import db
from .models import BmiRecords

# Create a Blueprint named 'views'
views = Blueprint('views', __name__)

# Define the welcome function for the homepage route
@views.route('/')
def welcome():
    return render_template('welcome.html', user=current_user)

# Define routes for other pages such as article, Categories, normal, obese, overweight, underweight
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

# Define a form class for BMI input
class MyForm(FlaskForm):
    height = TelField('Enter your height (m)', validators=[DataRequired()])
    weight = TelField('Enter your weight (Kg)', validators=[DataRequired()])
    submit = SubmitField('Submit')
    save_submit = SubmitField('Save and Submit')

@views.route('/bmi', methods=['GET', 'POST'])
# Ensure that the user is logged in to access this route
@login_required
def bmi():
    # Initialize variables
    height = weight = Categories = bmi_value = None
    # Create an instance of the MyForm class
    Form = MyForm()

    # If the form is submitted and passes validation
    if Form.validate_on_submit():
        try:
            height = float(Form.height.data)
            weight = float(Form.weight.data)
            now = f'{datetime.datetime.now().date().strftime("%d-%m-%Y")}'
            
            # Calculate the BMI value
            bmi_value = float(f'{weight / (height ** 2) * 10000 :.3f}')

            # Determine the BMI category based on the calculated BMI value
            if bmi_value >= 30:
                Categories = 'obese'
            elif 25 <= bmi_value < 30:
                Categories = 'overweight'
            elif 18.5 < bmi_value < 25:
                Categories = 'normal'
            elif bmi_value <= 18.5:
                Categories = 'underweight'

            # Flash a message based on whether the form was submitted or saved
            if Form.submit.data:
                flash('Calculation completed')
            elif Form.save_submit.data:
                flash('Calculation completed and Saved')
                # Create a new BmiRecords instance and add it to the database
                new_record = BmiRecords(user_id=current_user.id, weight=weight, height=height, bmi=bmi_value, categories=Categories, now=now)
                db.session.add(new_record)
                db.session.commit()
            
            # Clear form data
            Form.height.data = ''
            Form.weight.data = ''

        except ValueError:
            # Flash an error message for invalid input
            flash('Invalid input for height or weight', category='error')

    return render_template('bmi.html', form=Form, weight=weight, height=height, bmi=bmi_value, Categories=Categories, user=current_user)

@views.route('/account')
def account():
    # Get the user's data
    user = current_user
    email = user.email
    first_name = user.first_name
    # Query BMI records for the current user
    bmi_records = BmiRecords.query.filter_by(user_id=user.id).all()
    return render_template('account.html', user=user, email=email, first_name=first_name, bmi_records=bmi_records)
