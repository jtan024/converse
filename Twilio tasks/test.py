from firebase import firebase
firebase = firebase.FirebaseApplication(
    'https://converse-hacknow-a6513.firebaseio.com/', None)
# data =  { 'Name': 'Yash',
#           'RollNo': 1,
#           'Percentage': 76.02
#           }


def push_data(info):
    print(info)
    firebase.put('/', 'Test', info)
