from django.shortcuts import render
import requests
import pickle
import numpy as np
import sklearn
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "Jk3HUp_aUWSKvk9YehA_woUFyvn2BzgOxx_O957KanWp"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

def index(request):
    return render(request,"index.html")
def Prediction_admin(request):
    return render(request,"Prediction_admin.html")

def prediction(request):
    if request.method== 'POST':

        Year=int(request.POST['Year'])
        Year = 2022 - Year

        Present_Price=float(request.POST['Present_Price'])

        Kms_Driven=int(request.POST['Kms_Driven'])
        Kms_Driven2 = np.log(Kms_Driven)

        Owner=int(request.POST['Owner'])

        Fuel_Type_Petrol=request.POST['Fuel_Type_Petrol']
        if (Fuel_Type_Petrol == 'Petrol'):
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
            Fuel_Type_CNG = 0
        elif (Fuel_Type_Petrol == 'CNG'):
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0
            Fuel_Type_CNG = 1

        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1
            Fuel_Type_CNG = 0

        Seller_Type_Individual=request.POST['Seller_Type_Individual']
        if (Seller_Type_Individual == 'Individual'):
            Seller_Type_Individual = 1
            Seller_Type_Dealer =0
        else:
            Seller_Type_Individual = 0
            Seller_Type_Dealer = 1


        Transmission_Mannual=request.POST['Transmission_Mannual']
        if (Transmission_Mannual == 'Mannual'):
            Transmission_Mannual = 1
            Transmission_Automatic = 0
        else:
            Transmission_Mannual = 0
            Transmission_Automatic = 1
        if Year < 0:
            return render(request,'Prediction_admin.html',{'prediction_texts':"Sorry you cannot sell this car"})
        else:
            prediction  = {"input_data": [{"fields": [["Present_Price", "Kms_Driven2","Owner", "Year","Fuel_Type_CNG", "Fuel_Type_Diesel", "Fuel_Type_Petrol", 
                                    "Seller_Type_Dealer", "Seller_Type_Individual","Transmission_Automatic", "Transmission_Mannual"]], "values": [Present_Price, Kms_Driven2, Owner, Year,Fuel_Type_CNG, Fuel_Type_Diesel, Fuel_Type_Petrol, 
                                    Seller_Type_Dealer, Seller_Type_Individual,Transmission_Automatic, Transmission_Mannual]}]}

            response_scoring = requests.post('https://eu-de.ml.cloud.ibm.com/ml/v4/deployments/91bc857b-7b6f-46a8-bbc1-cc451dd8e958/predictions?version=2022-11-17', json=prediction,
            headers={'Authorization': 'Bearer ' + mltoken})
            print("Scoring response")
            print(response_scoring.json())
            output = round(prediction[0], 2)
            if output < 0:
                 return render(request,'Prediction_admin.html',{'prediction_texts':"Sorry you cannot sell this car"})
            else:
                contex={"output":output}
                return render(request,'Prediction.html',contex)
