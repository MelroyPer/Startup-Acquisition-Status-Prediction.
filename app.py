import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model_pipe.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():
    features = np.array([x for x in request.form.values()])
    print(features)
    input_df = pd.DataFrame(features.reshape(1,14),columns=['category_code', 'founded_at', 'country_code', 'first_funding_at', 'last_funding_at', 'funding_rounds', 'funding_total_usd', 'first_milestone_at', 'last_milestone_at', 'milestones', 'relationships', 'lat', 'lng', 'Active_Days'])    

    output = model.predict(input_df)
    print(output[0])
    if output[0] == 1:
        output = 'Closed'
    else:
        output = 'Operating'
    return render_template('index.html',prediction_test='The status of the company is : "{}"'.format(output))

if __name__ == "__main__":
    app.run(debug=True)