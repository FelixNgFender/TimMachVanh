import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import statsmodels.api as sm
from sklearn import linear_model

app = Flask(__name__)
model = pickle.load(open('trained_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict_proba(final_features)

    return render_template("index.html", prediction_text='Your chance of getting CHD in the next 10 years is {}'.format(prediction))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)