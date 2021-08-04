from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flora.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Kingdom(db.Model):
    __tablename__ = 'kingdom'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_plants = db.relationship('Plants', backref='k')


class Division(db.Model):
    __tablename__ = 'division'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_plants = db.relationship('Plants', backref='d')


class Class(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_plants = db.relationship('Plants', backref='c')


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_plants = db.relationship('Plants', backref='o')


class Family(db.Model):
    __tablename__ = 'family'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_plants = db.relationship('Plants', backref='f')


class Genus(db.Model):
    __tablename__ = 'genus'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_plants = db.relationship('Plants', backref='g')


class Plants(db.Model):
    __tablename__ = 'plants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    g_id = db.Column(db.Integer, db.ForeignKey('genus.id'))
    f_id = db.Column(db.Integer, db.ForeignKey('family.id'))
    o_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    c_id = db.Column(db.Integer, db.ForeignKey('class.id'))
    d_id = db.Column(db.Integer, db.ForeignKey('division.id'))
    k_id = db.Column(db.Integer, db.ForeignKey('kingdom.id'))


@app.route('/')
def func():
    return render_template("index.html", name="Россия")


@app.route('/two')
def func_two():
    return render_template("two.html")


@app.route('/flora', methods=['GET', 'POST'])
def data_base():
    if request.method == 'POST':
        data = Plants.query.filter(Plants.f_id.like(1))
        return render_template("flora.html", data=data)
    return render_template("flora.html")


if __name__ == '__main__':
    app.run(debug=True)
