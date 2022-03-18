from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('titanic_model_prediction_rf.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():

        Age = int(request.form['Age'])
        Fare = float(request.form['Fare'])
        Siblings = int(request.form['Siblings'])
        Parents = int(request.form['Parents'])
        Passenger_Class = int(request.form['Passenger_Class'])
        
        Gender = request.form['Gender']
        if(Gender=='Male'):
            Gender=1
        else:
            Gender=0
            
        Embarked = request.form['Embarked']
        if(Embarked=='Southampton'):
            Embarked_S=1
            Embarked_Q=0
        elif(Embarked=='Queenstown'):
            Embarked_S=0
            Embarked_Q=1
        else:
            Embarked_S=0
            Embarked_Q=0
            
        prediction=model.predict([[Age,Fare,Siblings,Parents,Passenger_Class,Gender,Embarked_S,Embarked_Q]])
        output=prediction[0]
        if output==1:
            return render_template('index.html',prediction_text="Passenger will survive")
        elif output==0:
            return render_template('index.html',prediction_text="Passenge will not survive, R.I.P")


if __name__=="__main__":
    app.run(debug=True)

