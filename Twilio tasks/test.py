from firebase import firebase
from flask import pyrebase
'''config = {
    "apiKey": "AIzaSyCkT9gwrOmLkV6SU1sfkq9Mwg3fFoLPAPc",
    "authDomain": "converse-hacknow-a6513.firebaseapp.com",
    "databaseURL": "https://converse-hacknow-a6513.firebaseio.com",
    "storageBucket": "converse-hacknow-a6513.appspot.com"
}
firebase = pyrebase.initalize_app(config)

database = firebase.database()
'''
firebase = firebase.FirebaseApplication(
    'https://converse-hacknow-a6513.firebaseio.com/', None)
# data =  { 'Name': 'Yash',
#           'RollNo': 1,
#           'Percentage': 76.02
#           }


def push_data(info):
    print(info)
    firebase.put('/', 'Test', info)
