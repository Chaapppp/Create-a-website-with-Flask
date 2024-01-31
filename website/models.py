from . import db
from flask_login import UserMixin

class BmiRecords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    bmi = db.Column(db.Float)
    categories = db.Column(db.String(50))
    now = db.Column(db.String(50))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    bmi_records = db.relationship('BmiRecords')
