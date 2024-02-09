from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from wtforms import TelField, SubmitField
from wtforms.validators import DataRequired
import datetime
from . import db
from .models import TXTRecords

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
    text = TelField('Enter here', validators=[DataRequired()])
    save_submit = SubmitField('Submit')

@views.route('/bmi', methods=['GET', 'POST'])
# Ensure that the user is logged in to access this route
@login_required
def bmi():
    # Initialize variables
    text = None
    # Create an instance of the MyForm class
    Form = MyForm()

    # If the form is submitted and passes validation
    if Form.validate_on_submit():
        try:
            text = str(Form.text.data)
            now = f'{datetime.datetime.now().date().strftime("%d-%m-%Y")}'
            
            if Form.save_submit.data:
                flash('Message Saved')
                # Create a new TxtRecords instance and add it to the database
                new_record = TXTRecords(user_id=current_user.id, text=text, now=now)
                db.session.add(new_record)
                db.session.commit()
                
            Form.text.data = ''

        except ValueError:
            # Flash an error message for invalid input
            flash('Invalid input', category='error')

    return render_template('bmi.html', form=Form, text=text, user=current_user)

@views.route('/account')
def account():
    # Get the user's data
    user = current_user
    email = user.email
    first_name = user.first_name
    # Query BMI records for the current user
    txt_records = TXTRecords.query.filter_by(user_id=user.id).all()
    return render_template('account.html', user=user, email=email, first_name=first_name, txt_records=txt_records)