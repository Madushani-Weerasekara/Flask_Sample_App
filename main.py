
# Intergrate HTML with Flask
# HTTP verb GET and POST
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

    return render_template('result.html', result=res)

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


# Result checker submit html page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score=0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = float(science+maths+c+data_science)/4

        res = ""

        if total_score>=100:
            res="success"
        else:
            res="fail"

        return redirect(url_for(res,score=total_score))




if __name__ == '__main__':
    app.run(debug=True, port=5001)