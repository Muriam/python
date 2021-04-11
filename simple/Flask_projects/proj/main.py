#вывод текста сюда http://127.0.0.1:5000/
from flask import Flask

app = Flask(__name__)

@app.route('/')

def func():
    return 'Tasmania is a beautiful island :)'

if __name__ == '__main__':
    app.run()
