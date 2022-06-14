from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('lr_model.pkl')

#If you're using any transformation
def transform(df):
	"""
	Your Transform here
	* return df
	"""
	pass

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
		age = request.args.get('age')
		grade = request.args.get('grade')
		s_class = request.args.get('class')
		level = request.args.get('level')

		#cast to int
		age = int(age)
		grade = int(grade)
		s_class = int(s_class)
		level = int(level)

		#for transform create with input data and pass df to transform function
		#df_new = transform(df);

		#make prediction
		pred = model.predict([[age, grade, s_class, level]]).tolist()
		return(jsonify(prediction=pred))
	except:
		return {"message":"ERROR!"}, 400

if __name__=="__main__":
	#debug=False for production use
	app.run(debug=True, host='0.0.0.0', port=9001)
