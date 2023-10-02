from flask import Flask,request,jsonify
import util
"""jsonify is a function provided by Flask that is used to convert Python dictionaries or 
objects into JSON format.
"""
app=Flask(__name__)

@app.route('/get_location_names')

def get_location_names():
    util.load_saved_artificats()
    response=jsonify({
        'location' : util.get_location_name()
    })
    response.headers.add("access-control-allow-origin",'*')
    return response

@app.route('/predict_home_price',methods=['host'])

def predict_home_price(): 
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=request.form['bhk']
    bath=int(request.form['bath'])

    response=jsonify({
        'estimated price' : util.predict_price(location,total_sqft,bath,bhk)
    })
    
    response.headers.add("access-control-allow-origin",'*')
    return response

if __name__=="__main__":
    print("starting python flask server for home price prediction")
    app.run()