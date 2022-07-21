from ast import Index
import numpy as np
from flask import Flask, request, render_template
import pickle
import ee
import collections

app = Flask(__name__)
model = pickle.load(open('model','rb'))
# find band values

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/',methods=['POST'])
def getLocation():

    starting = request.form['start']
    ending = request.form['end']
    print(starting+" == "+ending)

    location = request.form['location']

    print(location)
    l = location.split(",")
    l1 = l[0]
    l2 = l[1]
    lat = float(l1)
    lon = float(l2)
    collections.Callable = collections.abc.Callable
    service_account = 'muhammad402ali123@ee-afzal.iam.gserviceaccount.com'
    key = 'key.json'
    credentials = ee.ServiceAccountCredentials(service_account, key)
    ee.Initialize(credentials)

    p = ee.Geometry.Point([lon, lat])
    start = '2020-06-25'
    end = '2020-07-25'
    imageCollection = ee.ImageCollection('LANDSAT/LC08/C01/T1').filterDate(start, end).filterBounds(p)
    im1 = imageCollection.sort('CLOUD_COVER', True).first()
    data_b1 = im1.select("B1").reduceRegion(ee.Reducer.mean(),p,10).get("B1")
    b1 = (data_b1.getInfo())
    data_b1 = im1.select("B2").reduceRegion(ee.Reducer.mean(),p,10).get("B2")
    b2 = (data_b1.getInfo())
    data_b1 = im1.select("B3").reduceRegion(ee.Reducer.mean(),p,10).get("B3")
    b3 = (data_b1.getInfo())
    data_b1 = im1.select("B4").reduceRegion(ee.Reducer.mean(),p,10).get("B4")
    b4 = (data_b1.getInfo())
    data_b1 = im1.select("B5").reduceRegion(ee.Reducer.mean(),p,10).get("B5")
    b5 = (data_b1.getInfo())
    data_b1 = im1.select("B6").reduceRegion(ee.Reducer.mean(),p,10).get("B6")
    b6 = (data_b1.getInfo())
    data_b1 = im1.select("B7").reduceRegion(ee.Reducer.mean(),p,10).get("B7")
    b7 = (data_b1.getInfo())
    data_b1 = im1.select("B8").reduceRegion(ee.Reducer.mean(),p,10).get("B8")
    b8 = (data_b1.getInfo())
    data_b1 = im1.select("B9").reduceRegion(ee.Reducer.mean(),p,10).get("B9")
    b9 = (data_b1.getInfo())
    data_b1 = im1.select("B10").reduceRegion(ee.Reducer.mean(),p,10).get("B10")
    b10 = (data_b1.getInfo())
    data_b1 = im1.select("B11").reduceRegion(ee.Reducer.mean(),p,10).get("B11")
    b11 = (data_b1.getInfo()) 

    band = []
    band.append(b1)
    band.append(b2)
    band.append(b3)
    band.append(b4)
    band.append(b5)
    band.append(b6)
    band.append(b7)
    band.append(b9)
    band.append(b10)
    band.append(b11)  

    return render_template('Index.html',b1=b1,b2=b2,b3=b3,b4=b4,b5=b5,b6=b6,b7=b7,b9=b9,b10=b10,b11=b11)

   
@app.route('/getprediction',methods=['POST'])
def getprediction():    

    input = [float(x) for x in request.form.values()]
    final_input = [np.array(input)]
    prediction = model.predict(final_input)

    return render_template('Index.html', output='Your Soil Type is :{}'.format(prediction))
   

if __name__ == "__main__":
    app.run(debug=True)