from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Kinds(db.Model):
    __tablename__ = 'kinds'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    dragon = db.relationship('Dragonflies', backref='family')


class Dragonflies(db.Model):
    __tablename__ = 'dragonflies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    family_id = db.Column(db.Integer, db.ForeignKey('kinds.id'))


@app.route('/')
def func():
    return render_template("index.html", name="Россия")


@app.route('/two')
def func_two():
    return render_template("two.html")


@app.route('/fauna')
def data_base():
    data = Dragonflies.query.filter(Dragonflies.family_id.like(2))
    return render_template("fauna.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)
