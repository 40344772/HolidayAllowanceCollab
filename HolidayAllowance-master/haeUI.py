#HAEUI (Holiday Allowance Engine User Interface)
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home', methods=['POST', 'GET'])
def home():
    name = "Jane"
    return render_template('home.html' , name = name)

@app.route('/request')
def request():
    return render_template('request.html')

@app.route('/booked')
def booked():
    return render_template('booked.html')

if __name__ == "__main__":
    app.run(debug = True) #currently runs on debug mode to catch errors