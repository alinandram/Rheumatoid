from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/login")
@cross_origin(supports_credentials=True)
def login():
  return jsonify({'success': 'ok'})

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

import pickle
with open('finalized_model (1).sav','rb') as pickle_file:
  model = pickle.load(pickle_file)

import pandas as pd
def convertMapToPandasRow(x):
    return pd.DataFrame.from_dict(x)
    
import numpy as np   
@app.route('/mymodel', methods = ['POST'])
def hasRheumatioid():
    x = request.json
    pandasRow = convertMapToPandasRow(x)
    y= model.predict(pandasRow)
    return np.ndarray.tolist(y)

if __name__ == "__main__":
    app.run()



