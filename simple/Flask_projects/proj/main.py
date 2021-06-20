from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataBase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Insects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return '<Insects %r>' % self.id


@app.route('/')
def func():
    return render_template("index.html", name="Россия")


@app.route('/two')
def func_two():
    return render_template("two.html")


@app.route('/fauna', methods=['POST', 'GET'])
def func_three():
    if request.method == 'POST':
        name = request.form['name']

        insects = Insects(name=name)

        try:
            db.session.add(insects)
            db.session.commit()
            return redirect('/fauna')
        except:
            return "не получилось добавить запись"
    else:
        return render_template("fauna.html")


if __name__ == '__main__':
    app.run(debug=True)
