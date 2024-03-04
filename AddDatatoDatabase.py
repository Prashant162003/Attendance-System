import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase Details
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,
    {
    'databaseURL':"https://faceattendacerealtime-61547-default-rtdb.firebaseio.com/"
    }
)
ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Prashant Sagar Shakya",
            "major": "AI/ML",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "Good",
            "year": 3,
            "last_attendance_time": "2024-03-04 21:56:32"
        },
    "852741":
        {
            "name": "Vansh Bhandari",
            "major": "Data-Science",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "Good",
            "year": 3,
            "last_attendance_time": "2024-03-04 21:54:09"
        },
    "963852":
        {
            "name": "Mani Tyagi",
            "major": "Web-Dev",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "Good",
            "year": 3,
            "last_attendance_time": "2024-03-04 21:57:34"
        },
    "163959":
        {
            "name": "Aryan",
            "major": "Coding & Web",
            "starting_year": 2021,
            "total_attendance": 9,
            "standing": "Good",
            "year": 3,
            "last_attendance_time": "2024-03-04 21:50:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)