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


def transform(df):
	df['gender'] = df['gender'].map({'Male': 0,'Female' : 1}) 
	df['Self_Employed'] = df['Self_Employed'].map({'Yes' :1, 'No' : 0}), 
	df['Married'] = df['Married'].map({'No' : 0, 'Yes' :1})
	df['Education'] =  df['Education'].map({'Not Graduate' : 0, 'Graduate' : 1}),
	df['Property_Area'] = df['Property_Area'].map({'Urban' : 0, 'Rural' : 1, 'Semiurban' :2 }), 
	df['Dependents'] = df['Dependents'].map({'0' : 0, '1':1, '2':2, '3+' : 3})
	return df


@app.route('/')
@app.route('/index')
def home():
	""" Home View """

	return (jsonify(message="Welcome Home Gees!"))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
	"""
	Predict View
	Fit to suit your data/features
	"""
	try:

		#request args
		Gender = request.args.get('Gender')
		Married = request.args.get('Married')
		Dependents = request.args.get('Dependents')
		levelEducation = request.args.get('Education')
		Self_Employed = request.args.get('Self_Employed')
		Income = request.args.get('Income')
		Credit_History = request.args.get('Credit_History')
		Property_Area = request.args.get('Property_Area')
		Loan_Amount_Term = request.args.get('Loan_Amount_Term')
		Dependents_EMI_mean = request.args.get('Dependents_EMI_mean')
		Loan_Amount_Term_per_Total_Income = request.args.get('Loan_Amount_Term_per_Total_Income')
		EMI_Per_Loan_Amount_Term = request.args.get('EMI_Per_Loan_Amount_Term')
		EMI_Per_LoanAmount = request.args.get('EMI_Per_LoanAmount')
		Property_Area_LoanAmount_per_TotalIncome_mean = request.args.get('Property_Area_LoanAmount_per_TotalIncome_mean')
		Credit_History_Income_Sum = request.args.get('Credit_History_Income_Sum')
		Dependents_LoanAmount_Sum = request.args.get( 'Dependents_LoanAmount_Sum')
		Loan_Amount_Term_Bins = request.args.get('Loan_Amount_Term_Bins')
		TotalIncome_Bins = request.args.get('TotalIncome_Bins')

		#cast to int
		Gender = int(Gender)
		Married = int(Married)
		Dependents = int(Dependents)
		levelEducation = int(levelEducation)
		Self_Employed = int(Self_Employed)
		Income = int(Income)
		Credit_History = float(Credit_History)
		Property_Area = int(Property_Area)
		Loan_Amount_Term = float(Loan_Amount_Term)
		Dependents_EMI_mean = float(Dependents_EMI_mean)
		Loan_Amount_Term_per_Total_Income = float(Loan_Amount_Term_per_Total_Income)
		EMI_Per_Loan_Amount_Term = float(EMI_Per_Loan_Amount_Term)
		EMI_Per_LoanAmount = float(EMI_Per_LoanAmount)
		Property_Area_LoanAmount_per_TotalIncome_mean = float(Property_Area_LoanAmount_per_TotalIncome_mean)
		Credit_History_Income_Sum = int(Credit_History_Income_Sum)
		Dependents_LoanAmount_Sum = float(Dependents_LoanAmount_Sum)
		Loan_Amount_Term_Bins = float(Loan_Amount_Term_Bins)
		TotalIncome_Bins = float(TotalIncome_Bins)

		#for transform create with input data and pass df to transform function
		#df_new = transform(df);

		#make prediction
		pred = model.predict([[Gender,Married,Dependents,levelEducation,Self_Employed,Income,Credit_History,Property_Area,
							Loan_Amount_Term,Dependents_EMI_mean,Loan_Amount_Term_per_Total_Income,EMI_Per_Loan_Amount_Term,
							EMI_Per_LoanAmount,Property_Area_LoanAmount_per_TotalIncome_mean,Credit_History_Income_Sum,Dependents_LoanAmount_Sum,
							Loan_Amount_Term_Bins,TotalIncome_Bins]]).tolist()
		return(jsonify(prediction=pred))
	except:
		return {"message":"ERROR!"}, 400

if __name__=="__main__":
	#debug=False for production use
	app.run(debug=True, host='0.0.0.0', port=9001)