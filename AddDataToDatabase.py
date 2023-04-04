import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("service account key.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-attendance-89932-default-rtdb.firebaseio.com/"
    })

ref = db.reference('Students')

data = {
    "321654":
    {
           "name":" Murtaza ",
           "major": "Robotics" ,
           "starting_year":2017,
           "total_attendance": 7,
           "standing": "6",
           "year":4,
           "last_attendance_time": "2022-12-11 00:54:34"
    },       
    "852741":
    {
           "name":"Emly Blunt ",
           "major": "history" ,
           "starting_year":2010,
           "total_attendance": 17,
           "standing": "10",
           "year":3,
           "last_attendance_time": "2022-11-11 00:34:54"
    },       
     "963852":
    {
           "name":" Elon Musk ",
           "major": "Btech" ,
           "starting_year":2002,
           "total_attendance": 1,
           "standing": "1",
           "year":9,
           "last_attendance_time": "2021-12-11 00:54:34"
    },       
}

for key,value in data.items():
    ref.child(key).set(value)