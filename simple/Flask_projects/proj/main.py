from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flora.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_BINDS'] = {
    'fauna': 'sqlite:///fauna.db'
}
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


@app.route('/flora')
def flora():
    column1 = Plants.query.all()
    column2 = Genus.query.all()
    family_1 = Plants.query.filter(Plants.f_id.like(1))
    family_2 = Plants.query.filter(Plants.f_id.like(2))
    family_3 = Plants.query.filter(Plants.f_id.like(3))
    family_4 = Plants.query.filter(Plants.f_id.like(4))
    family_5 = Plants.query.filter(Plants.f_id.like(5))
    family_6 = Plants.query.filter(Plants.f_id.like(6))
    family_7 = Plants.query.filter(Plants.f_id.like(7))
    family_8 = Plants.query.filter(Plants.f_id.like(8))
    family_9 = Plants.query.filter(Plants.f_id.like(9))
    family_10 = Plants.query.filter(Plants.f_id.like(10))
    family_11 = Plants.query.filter(Plants.f_id.like(11))
    family_12 = Plants.query.filter(Plants.f_id.like(12))
    family_13 = Plants.query.filter(Plants.f_id.like(13))
    family_14 = Plants.query.filter(Plants.f_id.like(14))
    family_15 = Plants.query.filter(Plants.f_id.like(15))
    family_16 = Plants.query.filter(Plants.f_id.like(16))
    family_17 = Plants.query.filter(Plants.f_id.like(17))
    family_18 = Plants.query.filter(Plants.f_id.like(18))
    family_19 = Plants.query.filter(Plants.f_id.like(19))
    family_20 = Plants.query.filter(Plants.f_id.like(20))
    family_21 = Plants.query.filter(Plants.f_id.like(21))
    family_22 = Plants.query.filter(Plants.f_id.like(22))
    family_23 = Plants.query.filter(Plants.f_id.like(23))
    family_24 = Plants.query.filter(Plants.f_id.like(24))
    family_25 = Plants.query.filter(Plants.f_id.like(25))
    family_26 = Plants.query.filter(Plants.f_id.like(26))
    family_27 = Plants.query.filter(Plants.f_id.like(27))
    family_28 = Plants.query.filter(Plants.f_id.like(28))
    family_29 = Plants.query.filter(Plants.f_id.like(29))
    family_30 = Plants.query.filter(Plants.f_id.like(30))
    family_31 = Plants.query.filter(Plants.f_id.like(31))
    order_1 = Plants.query.filter(Plants.o_id.like(1))
    order_2 = Plants.query.filter(Plants.o_id.like(2))
    order_3 = Plants.query.filter(Plants.o_id.like(3))
    order_4 = Plants.query.filter(Plants.o_id.like(4))
    order_5 = Plants.query.filter(Plants.o_id.like(5))
    order_6 = Plants.query.filter(Plants.o_id.like(6))
    order_7 = Plants.query.filter(Plants.o_id.like(7))
    order_8 = Plants.query.filter(Plants.o_id.like(8))
    order_9 = Plants.query.filter(Plants.o_id.like(9))
    order_10 = Plants.query.filter(Plants.o_id.like(10))
    order_11 = Plants.query.filter(Plants.o_id.like(11))
    order_12 = Plants.query.filter(Plants.o_id.like(12))
    order_13 = Plants.query.filter(Plants.o_id.like(13))
    order_14 = Plants.query.filter(Plants.o_id.like(14))
    order_15 = Plants.query.filter(Plants.o_id.like(15))
    order_16 = Plants.query.filter(Plants.o_id.like(16))
    order_17 = Plants.query.filter(Plants.o_id.like(17))
    order_18 = Plants.query.filter(Plants.o_id.like(18))
    order_19 = Plants.query.filter(Plants.o_id.like(19))
    order_20 = Plants.query.filter(Plants.o_id.like(20))
    order_21 = Plants.query.filter(Plants.o_id.like(21))
    class_1 = Plants.query.filter(Plants.c_id.like(1))
    class_2 = Plants.query.filter(Plants.c_id.like(2))
    class_3 = Plants.query.filter(Plants.c_id.like(3))
    class_4 = Plants.query.filter(Plants.c_id.like(4))
    division_1 = Plants.query.filter(Plants.d_id.like(1))
    division_2 = Plants.query.filter(Plants.d_id.like(2))
    division_3 = Plants.query.filter(Plants.d_id.like(3))
    division_4 = Plants.query.filter(Plants.d_id.like(4))
    return render_template("flora.html", column1=column1, column2=column2, family_1=family_1, family_2=family_2,
                           family_3=family_3, family_4=family_4, family_5=family_5, family_6=family_6,
                           family_7=family_7, family_8=family_8, family_9=family_9, family_10=family_10,
                           family_11=family_11, family_12=family_12, family_13=family_13, family_14=family_14,
                           family_15=family_15, family_16=family_16, family_17=family_17, family_18=family_18,
                           family_19=family_19, family_20=family_20, family_21=family_21, family_22=family_22,
                           family_23=family_23, family_24=family_24, family_25=family_25, family_26=family_26,
                           family_27=family_27, family_28=family_28, family_29=family_29, family_30=family_30,
                           family_31=family_31, order_1=order_1, order_2=order_2, order_3=order_3, order_4=order_4,
                           order_5=order_5, order_6=order_6, order_7=order_7, order_8=order_8, order_9=order_9,
                           order_10=order_10, order_11=order_11, order_12=order_12, order_13=order_13,
                           order_14=order_14, order_15=order_15, order_16=order_16, order_17=order_17,
                           order_18=order_18, order_19=order_19, order_20=order_20, order_21=order_21,
                           class_1=class_1, class_2=class_2, class_3=class_3, class_4=class_4, division_1=division_1,
                           division_2=division_2, division_3=division_3, division_4=division_4)


class Kingdom2(db.Model):
    __tablename__ = 'kingdom2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_plants = db.relationship('Species2', backref='k')


class Phylum2(db.Model):
    __tablename__ = 'phylum2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_plants = db.relationship('Species2', backref='d')


class Class2(db.Model):
    __tablename__ = 'class2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_plants = db.relationship('Species2', backref='c')


class Order2(db.Model):
    __tablename__ = 'order2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_plants = db.relationship('Species2', backref='o')


class Family2(db.Model):
    __tablename__ = 'family2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_plants = db.relationship('Species2', backref='f')


class Genus2(db.Model):
    __tablename__ = 'genus2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    with_plants = db.relationship('Species2', backref='g')


class Species2(db.Model):
    __tablename__ = 'species2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    genus2_id = db.Column(db.Integer, db.ForeignKey('genus2.id'))
    family2_id = db.Column(db.Integer, db.ForeignKey('family2.id'))
    order2_id = db.Column(db.Integer, db.ForeignKey('order2.id'))
    class2_id = db.Column(db.Integer, db.ForeignKey('class2.id'))
    phylum2_id = db.Column(db.Integer, db.ForeignKey('phylum2.id'))
    kingdom2_id = db.Column(db.Integer, db.ForeignKey('kingdom2.id'))
    info = {'bind_key': 'genus2'}


if __name__ == '__main__':
    app.run(debug=True)
