
# Intergrate HTML with Flask
# HTTP verb GET and POST


# jinja2 template engine
import os
import jinja2


"""
{%...%} conditions, for loops
{{}} expression to print output
{{#....#}}this is for comment

"""

from flask import Flask, redirect, url_for, render_template,request

# wsgi application
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/members')
def members():
    return 'Hellow Members'

# Building urls dynamically
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template('result.html', result=score)

@app.route('/fail/<int:score>')
def fail(score):
   
    return 'The person is fail and the mark is ' + str(score)
"""
# Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ''
    if marks<=50:
        result= 'fail'
    else:
        result = 'success'
    #return result
    return redirect(url_for(result,score=marks))"""


# Result checker submit html page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science) / 4

        if total_score >= 50:
            return redirect(url_for('success', score=total_score))
        else:
            return redirect(url_for('fail', score=total_score))


if __name__ == '__main__':
    app.run(debug=True, port=5001)