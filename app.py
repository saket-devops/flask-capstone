from flask import Flask, render_template, url_for, request, redirect


import sys
sys.path.append('G:\Work Profile\Flask\Capstone Project - I')

import saket_raw_code_fun
from saket_raw_code_fun import predict

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])     
def index():
        return render_template("index.html",cgpa=None)

@app.route('/calc',methods=['POST','GET'])
def delete():
   if(request.method == 'POST'):
       p3=[]
       p3.append(int(request.form['Attendance']))
       p3.append(int(request.form['Study']))
       p3.append(int(request.form['avgstu']))
       p3.append(int(request.form['holiday']))
       p3.append(int(request.form['hostel']))
       p3.append(int(request.form['mess']))
       p3.append(int(request.form['drin']))
       p3.append(int(request.form['relation']))
       p3.append(int(request.form['edu']))
       p3.append(int(request.form['parent']))
       p3.append(int(request.form['phy']))
       p3.append(int(request.form['club']))
       p3.append(int(request.form['media']))
       var=[]
       var.append(p3)
       CGPA=predict(var)
       return render_template('model.html',cgpa=CGPA)

@app.route("/home")
def index2():
    return render_template("index.html", cgpa=None)

@app.route("/model")
def index3():
    return render_template("model.html", cgpa=None)

@app.route("/form")
def index4():
    return render_template("form.html", cgpa=None)

@app.route("/about")
def index5():
    return render_template("about us.html", cgpa=None)

if __name__ == "__main__":
    app.run(debug=True) 