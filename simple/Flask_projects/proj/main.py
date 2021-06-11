from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
db = SQLAlchemy


@app.route('/')
def func():
    return render_template("index.html", name="Россия")


@app.route('/two')
def func_two():
    return render_template("two.html")


@app.route('/fauna')
def func_three():
    return render_template("fauna.html")


if __name__ == '__main__':
    app.run(debug=True)
