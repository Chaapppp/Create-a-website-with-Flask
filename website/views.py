from flask import Blueprint ,render_template
from flask_login import login_required

views = Blueprint('views',__name__)

@views.route('/')
def welcome():
    return render_template('welcome.html')

@views.route('/account')
def account():
    return render_template('account.html')

@views.route('/article')
def article():
    return render_template('article.html')

@views.route('/Categories')
def Categories():
    return render_template('Categories.html')

@views.route('/normal')
def normal():
    return render_template('normal.html')

@views.route('/obese')
def obese():
    return render_template('obese.html')

@views.route('/overweight')
def overweight():
    return render_template('overweight.html')










@views.route('/bmi')
@login_required
def bmi():
    return render_template('bmi.html')
