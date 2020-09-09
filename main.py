## https://codelabs.developers.google.com/codelabs/cloud-vision-app-engine/index.html?index=..%2F..index#1

### GCP - akash9129@gmail.com; Akashram1@
### This app was deployed to gcp -- so follow this structure, 
### GCP valid till dec and then can create a new id and get same free with that ID


### DB used was elephant sql -- was easy to set up and also make db-app engine talk , cloudsql was really annoying so didnt bother

### Cloud sql problem was with instance location -- apparently both app engine and cloud sql have to be at the same location..

### Run ./cloud_sql_proxy -instances=santander-recommendation:us-central1:santander=tcp:4500 to run the app locally
### and also check if your public needs to be added, this is only for local

from db import getCustomerDetails, open_connection, get_songs
from flask import Flask, request, render_template
import json
import pickle
import numpy as np 
import joblib
import sklearn
from sklearn.linear_model import LogisticRegression

#model = pickle.loads(rff    ) 

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
    return render_template('result.html', Personal_Loan_Val=pr) #, Personal_Loan_Sts= str(int(float(pl[1])*100)) + '%', CC_Val= cc[0], CC_Sts = str(int(float(cc[1])*100)) + '%',HL_Val = hl[0], HL_Sts = str(int(float(hl[1])*100)) +'%' , CL_Val = vl[0], CL_Sts = str(int(float(vl[1])*100)) + '%', BL_Val = vl[0], BL_Sts = str(int(float(vl[1])*100)) + '%')

if __name__ == '__main__':
    app.run(debug=True)
