from flask import Blueprint ,render_template, flash
from flask_login import login_required, current_user
from flask_wtf import FlaskForm
from wtforms import TelField, SubmitField
from wtforms.validators import DataRequired
import datetime 
from . import db
from .models import BmiRecords


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

    if Form.validate_on_submit():
        try:
            height = float(Form.height.data)
            weight = float(Form.weight.data)
            now = f'{((datetime.datetime.now()).date()).strftime("%d-%m-%Y")}'\
            
            bmi_value = float(f'{weight / (height ** 2) * 10000 :.3f}')

            if bmi_value >= 30:
                Categories = 'obese'
            elif 25 <= bmi_value < 30:
                Categories = 'overweight'
            elif 18.5 < bmi_value < 25:
                Categories = 'normal'
            elif bmi_value <= 18.5:
                Categories = 'underweight'

            if Form.submit.data:
                flash('Calculation completed')
            elif Form.save_submit.data:
                flash('Calculation completed and Saved')
                new_record = BmiRecords(user_id=current_user.id, weight=weight, height=height, bmi=bmi_value, categories=Categories,now=now)
                db.session.add(new_record)
                db.session.commit()


        except ValueError:
            flash('Invalid input for height or weight', category='error')

    return render_template('bmi.html', form=Form, weight=weight, height=height, bmi=bmi_value, Categories=Categories, user=current_user)

