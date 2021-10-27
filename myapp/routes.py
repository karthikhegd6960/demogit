
from myapp import app,mysql
from flask import render_template,url_for,redirect,request
from myapp.forms import CreditForm,RegisterForm,LoginForm


from datetime import date, datetime
import matplotlib.pyplot as plt
import numpy as np




@app.route("/")
@app.route("/home",methods=['GET','POST'])
def home():

 
    return render_template ('home.html',title='home')

@app.route("/enter",methods=['GET',"POST"])
def enter():
    if request.method=='POST':
        details = request.form
        amount = details['amount']
        transaction_type = details['transaction_type']
        Transaction_by=details['Transaction_by']
        purpose=details['purpose']
        form_of_transaction=details['form_of_transaction']
        transaction_date= str(date.today())
        

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO saving (amount,transaction_type,Transaction_by,purpose,form_of_transaction,transaction_date) VALUES(%s,%s,%s,%s,%s,%s)",(amount, transaction_type,Transaction_by,purpose,form_of_transaction,transaction_date))
        mysql.connection.commit()
        cur.close()
        
    return render_template('enter.html')

@app.route('/about',methods=['GET','POST'])
def about():
   

    return render_template ('about.html',title='about')

@app.route('/Register',methods=['GET','POST'])
def Register():
    form=RegisterForm()

    return render_template('register.html',title='register',form=form)

@app.route('/Login',methods=['GET','POST'])
def Login():
    if request.method=='POST':
        details=request.form
        email=details['email']
        password=details['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO login (email,password) VALUES(%s,%s)",(email,password))
        mysql.connection.commit()
        cur.close()



    
    return render_template('login.html',title='login')

@app.route('/pie',methods=['GET','POST'])
def pie():
    if request.method=='POST':
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM saving")
        

    