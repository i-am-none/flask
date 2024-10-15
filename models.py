from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Individual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    income = db.Column(db.Float, nullable=False)

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    revenue = db.Column(db.Float, nullable=False)
    employees = db.Column(db.Integer, nullable=False)

class IndividualContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.JSON, nullable=False)

class BusinessContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.JSON)
