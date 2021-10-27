from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
engine = create_engine("sqlite:///db.db")
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


class Kingdom(db.Model):
    __tablename__ = 'kingdom'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_species = db.relationship('Species', backref='kingdom')


class DivisionOrPhylum(db.Model):
    __tablename__ = 'divisionOrPhylum'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_species = db.relationship('Species', backref='divisionOrPhylum')


class Class(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_species = db.relationship('Species', backref='class')


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_species = db.relationship('Species', backref='order')


class Family(db.Model):
    __tablename__ = 'family'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_species = db.relationship('Species', backref='family')


class Genus(db.Model):
    __tablename__ = 'genus'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_species = db.relationship('Species', backref='genus')


class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    genus_id = db.Column(db.Integer, db.ForeignKey('genus.id'))
    family_id = db.Column(db.Integer, db.ForeignKey('family.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))
    divisionOrPhylum_id = db.Column(db.Integer, db.ForeignKey('divisionOrPhylum.id'))
    kingdom_id = db.Column(db.Integer, db.ForeignKey('kingdom.id'))


@app.route('/')
def func():
    return render_template("index.html", name='Россия')


@app.route('/two')
def func_two():
    return render_template("two.html")


class TestForm(FlaskForm):
    queryUser = StringField('enter your query')
    button = SubmitField('send')


@app.route('/flora', methods=['GET', 'POST'])
def flora():
    form = TestForm()
    if form.validate_on_submit():
        query_from_form = form.queryUser.data
        kingdom = ['растения', 'животные']
        if query_from_form in kingdom[0]:
            query = db.engine.execute('SELECT * FROM Species WHERE kingdom_id=1')
            return render_template('flora.html', query=query, form=form)
        elif query_from_form == kingdom[1]:
            query = db.engine.execute('SELECT * FROM Species WHERE kingdom_id=2')
            return render_template('flora.html', query=query, form=form)
    return render_template('flora.html', form=form)


@app.route('/fauna')
def fauna():
    data = Species.query.filter(Species.kingdom_id.like(2))
    return render_template("fauna.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)
