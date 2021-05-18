from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def func():
    d = {'Населенные пункты': 'Хобарт', 'Флора': 'Молочай тирукалли', 'Фауна': 'Тонкоклювый буревестник'}
    return render_template("index.html", name="Австралия", d=d)


if __name__ == '__main__':
    app.run(debug=True)
