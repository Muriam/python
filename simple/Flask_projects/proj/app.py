from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


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
    return render_template("index.html", name="Россия")


@app.route('/two')
def func_two():
    return render_template("two.html")


@app.route('/flora')
def flora():
    data = Species.query.all()
    query = db.engine.execute("<SELECT * FROM Family>")
    return render_template("flora.html", data=data, query=query)


@app.route('/fauna')
def fauna():
    data2 = Species.query.filter(Species.kingdom_id.like(2))
    return render_template("fauna.html", data2=data2)


if __name__ == '__main__':
    app.run(debug=True)
