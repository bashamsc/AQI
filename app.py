from flask import Flask
from flask import request,render_template,url_for
import pickle

app=Flask(__name__)

model = pickle.load(open('lasso_regression_model.pkl', 'rb'))

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	AQI_predict = None
	if request.method == 'POST':
		# field1 = request.form['field1']
		AQI_predict=model.predict([[
			request.form["PM2.5"],
			request.form["PM10"],
			request.form["NO2"],
			request.form["SO2"],
			request.form["CO"]
			
		]])    
	
	return render_template('result.html', prediction=AQI_predict)

if __name__=='__main__':
	app.run()
