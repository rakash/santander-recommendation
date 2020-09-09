from db import getCustomerDetails, open_connection, get_songs
from flask import Flask, request, render_template
import json
import pickle
import numpy as np 
import joblib
import sklearn
from sklearn.linear_model import LogisticRegression

file = open("rff1.pkl", 'rb')
rff = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('result.html')
    
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['search']
    variable=getCustomerDetails(text)
    v = variable[0]
    v.pop(0)
    pr = np.array(v).reshape(1, -1)
    pr = rff.predict(pr)
    pr = pr[0]
    if pr==0:
        pr='No'
    else:
        pr='yes'
    return render_template('result.html', Personal_Loan_Val=pr)

if __name__ == '__main__':
    app.run(debug=True)
