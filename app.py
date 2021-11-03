from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crear la aplicación en flask
app = Flask(__name__)
# Configuración de la bd
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# Asociar nuestra bd con la aplicación en flask
db = SQLAlchemy(app)


# Model
class Enterprise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable=False)
    created = db.Column(db.Integer)

    # una representación de cadena de caracteres
    def __repr__(self):
        return f'{self.name}'


# Create db from python console
# from app import db
# db.create_all()
# from app import Enterprise
# google = Enterprise(name='google', created=2020)
# facebook = Enterprise(name='facebook', created=2021)
# db.session.add(google)
# db.session.add(facebook)
# db.session.commit()
# Enterprise.query.all()

# many to many between: developer and languaje
languajes_developer = db.Table('languajes_developer',
                               db.Column('languaje_id', db.Integer, db.ForeignKey('languaje.id'), primary_key=True),
                               db.Column('developer.id', db.Integer, db.ForeignKey('developer.id'), primary_key=True))


# holger = Developer(name='holger', age=35, enterprise=google)
# db.session.add(holger)
# db.session.commit()
class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    enterprise_id = db.Column(db.Integer, db.ForeignKey('enterprise.id'))
    # Crear la relación entre la columna y el modelo
    enterprise = db.relationship('Enterprise', backref=db.backref('developer', lazy=True))
    languajes = db.relationship('Languaje', secondary=languajes_developer, backref=db.backref('developers', lazy=True))

    def __repr__(self):
        return f'{self.name}'


class Languaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'{self.name}'

# java = Languaje(name='java')
# python = Languaje(name='python')
# db.session.add(java)
# db.session.add(python)
# db.session.commit()
# Languaje.query.all()


#join
#db.session.query(Developer).join(Enterprise).filter(Enterprise.name=='google').first()