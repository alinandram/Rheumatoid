from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

import pickle
with open('finalized_model.sav','rb') as pickle_file:
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

app.run()



