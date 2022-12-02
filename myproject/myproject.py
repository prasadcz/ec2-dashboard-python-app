import uuid
import requests
from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session  # https://pythonhosted.org/Flask-Session
import script1


app = Flask(__name__,template_folder='templates')

@app.route("/")
def login():
      return render_template('login.html')

@app.route('/index.html', methods = ['POST', 'GET'])
def index1():
    list = ["prasad","vivekananda"]
    output = request.form.to_dict()
    name = output['name']
    if name in list:
      return render_template('index.html')
    else:
      return render_template('error.html')
      
     
@app.route('/table.html', methods = ['POST', 'GET'])
def myfun():
    output = request.form.to_dict()
    name = output['tvalue']
    reg = output['rvalue']
    ser = output['svalue']
    if ser == 'ec2':
      if name == "Main":
        script1.ec2(name, reg)
        return render_template('table.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=33322,debug=True)


