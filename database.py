from pymongo import MongoClient
import datetime
import numpy as np

client = MongoClient('mongodb://localhost:27017/')
db = client['medical_data']
collection = db['seizures']

def save_to_db(temp, light, hum, co2, acc, is_seizure):
    print(temp, light, hum, co2)
    seizure = {'time':datetime.datetime.utcnow(),
        'is_seizure':is_seizure,
        'humidity':hum,
        'air_quality':co2,
        'temperature':temp,
        'light':light,
        'accelerometer':acc}

    collection.insert_one(seizure)

# cur = collection.find({})
# for doc in cur:
#      print(doc)