
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '123456'



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/input', methods=['POST'])
def create_user():
    print("Got input Info")
    session['username'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['favorite language']
    session['comment'] = request.form['comment']
    return redirect('/result') 
    


@app.route('/result')
def show_user():
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)