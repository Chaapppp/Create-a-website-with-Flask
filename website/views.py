from flask import Blueprint

views = Blueprint('views',__name__)

@views.route('/')
def welcome():
    return '<p>welcome</p>'