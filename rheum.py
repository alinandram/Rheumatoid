#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

import cors from 'cors';

CORS(app, support_credentials=False)
@app.route('/')
def hello_world():
    return 'Hello, World!'

import pickle
with open('xGBoost_model.sav','rb') as pickle_file:
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


# In[ ]:




