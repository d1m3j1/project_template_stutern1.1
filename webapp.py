from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('auction_model.pkl')


@app.route('/')
@app.route('/index')
def home():
	""" Home View """

	return (jsonify(message="Welcome Home Gees!"))

@app.route('/predict', methods=['GET', 'POST'])
def predict():

	try:

		#request args
		Gender = request.args.get('Gender')
		Married = request.args.get('Married')
		Dependents = request.args.get('Dependents')
		Graduate = request.args.get('Graduate')
		Self_Employed = request.args.get('Self_Employed')
		Income = request.args.get('Income')
		state = request.args.get('Property_Area')
		if state in ['Abuja','Lagos', 'Port Harcourt']:
			Property_Area = 'Urban'
		elif state in ['Kano','Kwara', 'Oyo' , 'Ogun' , 'Cross River', 'Imo']:
			Property_Area ='Semiurban'
		else: 
			Property_Area ='Rural'	
		Prev_Credit_Dur = request.args.get('Prev_Credit_Dur')
		Total_Amount_Spent = request.args.get('Total_Amount_Spent')
		hist = request.args.get('Credit_History')
		if hist in ['Yes']:
			Credit_History = 1
		else : 
			Credit_History = 0
		
		#cast to required datatypes
		Gender = str(Gender)
		Married = str(Married)
		Dependents = int(Dependents)
		Graduate = str(Graduate)
		Self_Employed = str(Self_Employed)
		Income = int(Income)
		Property_Area = str(Property_Area)
		Prev_Credit_Dur = int(Prev_Credit_Dur)
		Total_Amount_Spent = float(Total_Amount_Spent)
		Credit_History = str(Credit_History)

		#make prediction
		pred = model.predict([[Gender,Married,Dependents,Graduate,Self_Employed,Income,Property_Area, Prev_Credit_Dur,Total_Amount_Spent,Credit_History]]).tolist()
		return(jsonify(prediction=pred))
	except:
		return {"message":"ERROR!"}, 400

if __name__=="__main__":
	#debug=False for production use
	app.run(debug=True, host='0.0.0.0', port=9001)