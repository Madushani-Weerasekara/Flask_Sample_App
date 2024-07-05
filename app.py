
from flask import Flask, redirect, url_for

# wsgi application
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello Flask'

@app.route('/members')
def members():
    return 'Hellow Members'

# Building urls dynamically
@app.route('/success/<int:score>')
def success(score):
    return 'The person is pass and the mark is ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person is fail and the mark is ' + str(score)

# Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ''
    if marks<=50:
        result= 'fail'
    else:
        result = 'success'
    #return result
    return redirect(url_for(result,score=marks))

if __name__ == '__main__':
    app.run(debug=True, port=5001)