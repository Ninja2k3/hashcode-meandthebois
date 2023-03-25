import pyrebase

config = {
    "apiKey": "AIzaSyDybkQ-gyeyXoXZlF8fy26Y5JXo4svBq6Y",
    "authDomain": "parking-management-4e32d.firebaseapp.com",
    "projectId": "parking-management-4e32d",
    "databaseURL": "https://parking-management-4e32d-default-rtdb.firebaseio.com/",
    "storageBucket": "parking-management-4e32d.appspot.com",
    "messagingSenderId": "1091771919954",
    "appId": "1:1091771919954:web:1fa7d43eecdf4e6cdd798b",
    "measurementId": "G-QQ1YN4MW68"
}

firebase=pyrebase.initialize_app(config)

db=firebase.database()

db.child("names").push({"name":"PESU"})