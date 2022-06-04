
from flask import Flask,request,jsonify,render_template,url_for
import pickle
import pandas as pd
import numpy as np
from flask_cors import CORS,cross_origin

app=Flask(__name__)

model=pickle.load(open('projectmodel.pkl','rb'))

@app.route('/',methods=['POST','GET'])
@cross_origin()

def home():
    #return 'Hello World'
    return render_template('home.html')

@app.route('/postman_api',methods=['POST'])
@cross_origin()

def test():

    data=request.json['data']
    print(data)
    newdata=[list(data.values())]
    output=newdata[0]
    return jsonify(output)

@app.route('/predict',methods=['POST'])
@cross_origin()

def test1():

    data1=[float(i) for i in request.form.values()]
    data2=[np.array(data1)]
    print(data1)
    output=model.predict(data2)[0]
    print(output)
    return render_template('home.html',prediction_text='The forest is {} /n 1-fired,0-Not fired'.format(output))

if __name__=='__main__':
    app.run(debug=True)
     




