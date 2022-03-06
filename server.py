from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "top secret"  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    session['value1'] = request.form['strawberry']
    session['value2'] = request.form['raspberry']
    session['value3'] = request.form['apple']
    session['sum'] = int(request.form['apple'])+int(request.form['raspberry'])+int(request.form['strawberry'])
    return redirect('/checkout')

@app.route('/checkout')         
def checkoutresult():
    return render_template("checkout.html") 

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    