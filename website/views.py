from flask import Blueprint ,render_template
from flask_login import login_required, current_user

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









@views.route('/bmi')
@login_required
def bmi():
    return render_template('bmi.html', user=current_user)
