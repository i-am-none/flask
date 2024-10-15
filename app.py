from __future__ import annotations

import logging
import os
import sys
import typing as t
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from routes.individual_routes import individual
from routes.business_routes import business
from routes.home_routes import home

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taxplan.db'
db.init_app(app)

app.register_blueprint(individual)
app.register_blueprint(business)
app.register_blueprint(home)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
