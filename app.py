import numpy as np
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('prediction.html')

@app.route('/predict')
def predict():
    model = joblib.load('C:\\Users\\Sanjay\\OneDrive\\Documents\\app\\env\\model.joblib')
    if request.args.get('ph') == 'Male':
        temp=1
    else:
        temp=0
        
    sslc=float(request.args.get('sslc'))
    
    if request.args.get('stream') == 'Commerce':
        temp1=1
    elif request.args.get('stream') == 'Science':
        temp1=2
    else:
        temp1=0
    pu=float(request.args.get('pu'))
    if request.args.get('deg') == 'Comm and Mgmt':
        temp2=0
    elif request.args.get('deg') == 'science and tech':
        temp2=2
    else:
        temp2=1
    degree=float(request.args.get('degree'))
    if request.args.get('wex') == 'Yes':
        temp3=1
    else:
        temp3=0

    data = [temp,sslc,pu,temp1,degree,temp3,temp2]
    print(data)
    result = model.predict(np.array(data).reshape(1,-1))
    if result[0] == 1:
        resFile = open('C:\\Users\\Sanjay\\OneDrive\\Documents\\app\\env\\congrats.html').read()
    else:
        resFile = open('C:\\Users\\Sanjay\\OneDrive\\Documents\\app\\env\\sad.html').read()
        
    return resFile

    