# util will contain all the routine wherever server yet do the routine to request and respnse
import json 
import pickle 
import numpy as np 
__location=None
__data_columns=None
__model=None

# here above we have created the global variable 


def predict_price(location,sqft,bath,bhk):   
    try:
        loc_index =__data_columns.index(location.lower())
    except:
            loc_index=-1


    X = np.zeros(len(__data_columns))
    X[0] = sqft
    X[1] = bath
    X[2] = bhk
    if loc_index >= 0:
        X[loc_index] = 1

    return round(__model.predict([X])[0],2)


def get_location_name():
    return __location

def load_saved_artificats():
    print("loading saved artificats..start")
    global __data_columns
    global __location

    with open(r"C:\Users\hp\Desktop\data sciene\machine learning\project 1\BHP\server\artificat\banglore_home_price_model_coloum.json",'r' ) as f:
        __data_columns=json.load(f)["columns"]
        __location=__data_columns[3:]

    global __model


    with open(r"C:\Users\hp\Desktop\data sciene\machine learning\project 1\BHP\server\artificat\banglore_home_prices_model.pickle",'rb') as f:
        __model=pickle.load(f)

    print("loading the artificat is done")


    
if(__name__=='__main__'):
    load_saved_artificats()
    print(get_location_name())
    print(predict_price('1st Phase JP Nagar',1000, 2, 2))
    print(predict_price('other',1000,2,2))


#project 1\BHP\server\artificat\banglore_home_price_model_coloum.json
#C:\Users\hp\Desktop\data sciene\machine learning\project 1\BHP\server\artificat\banglore_home_price_model_coloum.json
#project 1\BHP\server\artificat\banglore_home_prices_model.pickle
#C:\Users\hp\Desktop\data sciene\machine learning\project 1\BHP\server\artificat\banglore_home_prices_model.pickle