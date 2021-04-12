#http://127.0.0.1:5000/
#размещение html и css и прочего
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def func():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
