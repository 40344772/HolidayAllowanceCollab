#HAEUI (Holiday Allowance Engine User Interface)
from flask import Flask, render_template, url_for

app = Flask(__name__) 

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def index():
    return render_template('request.html')

if __name__ == "__main__":
    app.run(debug = True) #currently runs on debug mode to catch errors