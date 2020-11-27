from datetime import date
import json
import pymongo
import  random
from currencies import parseData
import pandas as pd

def data_from_db():
    data = parseData()
    new = data.to_json()

    data['Date'] = pd.to_datetime(data['Date'])
    client = pymongo.MongoClient("mongodb+srv://gauss:010505de@cluster0.0xkv2.mongodb.net/currencies_db?retryWrites=true&w=majority")
    db = client.list_database_names()
    mydb = client['currencies']
    mycol = mydb['currencies_db']

    # x = mycol.insert_many(data.to_dict('records'))
    list_of_x = []
    list_of_name =[]
    date_extras = []

    for x in mycol.find():


        list_of_x.append(x['Cumparare USD'])
        list_of_name.append(x['Denumirea Bancii'])
        # x['Cumparare USD'] = float(x['Cumparare USD'])
        date_extras.append(x['Date'])


    res = [r.replace(',', '.') for r in list_of_x]
    res = [float(n) for n in res]


    ######

    tab1 = (list(zip(list_of_name,res,date_extras )))

    db_data = pd.DataFrame(tab1, columns=['Denumirea Bancii','Cumparare USD', 'Date_Now'])

    return db_data








