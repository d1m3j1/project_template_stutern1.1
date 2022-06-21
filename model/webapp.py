from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('auction_model.pkl')

#If you're using any transformation
def handle_data(df):
	def state(df) -> pd.DataFrame:
		if (df['State'] == 'Abuja') | (df['State'] == 'Lagos') | (df['State'] == 'Port Harcourt'):
			return 'Urban'
		elif (df['State'] == 'Kano') | (df['State'] == 'Kwara') | (df['State'] == 'Oyo') | (df['State'] == 'Ogun') | (df['State'] == 'Cross River') | (df['State'] == 'Imo'):
			return 'Semiurban'
		else: 
			return 'Rural'
		
	df['Property_Area'] = [state(i) for i in df['State']]
	df.drop('State', axis = 1, inplace = True)
	return df


# def transform(df):
# 	df['gender'] = df['gender'].map({'Male': 0,'Female' : 1}) 
# 	df['Self_Employed'] = df['Self_Employed'].map({'Yes' :1, 'No' : 0}), 
# 	df['Married'] = df['Married'].map({'No' : 0, 'Yes' :1})
# 	df['Education'] =  df['Education'].map({'Not Graduate' : 0, 'Graduate' : 1}),
# 	df['Property_Area'] = df['Property_Area'].map({'Urban' : 0, 'Rural' : 1, 'Semiurban' :2 }), 
# 	df['Dependents'] = df['Dependents'].map({'0' : 0, '1':1, '2':2, '3+' : 3})
# 	return df


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
		Property_Area = request.args.get('Property_Area')
		Prev_Credit_Dur = request.args.get('Prev_Credit_Dur')
		Total_Amount_Spent = request.args.get('Total_Amount_Spent')
		Credit_History = request.args.get('Credit_History')
		

		#cast to required datatypes
		Gender = str(Gender)
		Married = str(Married)
		Dependents = int(Dependents)
		Graduate = str(Graduate)
		Self_Employed = str(Self_Employed)
		Income = int(Income)
		Property_Area = str(Property_Area)
		Prev_Credit_Dur = float(Prev_Credit_Dur)
		Total_Amount_Spent = float(Total_Amount_Spent)
		Credit_History = float(Credit_History)

		#for transform create with input data and pass df to transform function
		#df_new = transform(df);

		#make prediction
		pred = model.predict([[Gender,Married,Dependents,Graduate,Self_Employed,Income,Property_Area,
							Prev_Credit_Dur,Total_Amount_Spent,Credit_History]]).tolist()
		return(jsonify(prediction=pred))
	except:
		return {"message":"ERROR!"}, 400

if __name__=="__main__":
	#debug=False for production use
	app.run(debug=True, host='0.0.0.0', port=9001)