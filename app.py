
from flask import Flask

# wsgi application
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello Flask'

@app.route('/members')
def members():
    return 'Hellow Members'




if __name__ == '__main__':
    app.run(debug=True)