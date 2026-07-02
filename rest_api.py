from fastapi import FastAPI

import pickle

app=FastAPI()

modelPickle=open("./artifacts/classifier1.pkl","rb")
clf=pickle.load(modelPickle)

@app.get("/")
async def root():
    return {"Message":"Hi, I am up and working"}



@app.post('/predict')
def prediction(loan_req: dict):
    # Pre-processing user input
    print(loan_req) 

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
 
    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
    
    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount'] / 1000
 
    # Making predictions 
    prediction = clf.predict( 
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'

    result = {
        'loan_approval_status': pred
    }

    return result
