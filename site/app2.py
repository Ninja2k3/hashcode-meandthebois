from flask import Flask,render_template,Response,request,redirect,url_for
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

app=Flask(__name__)



@app.route('/newlocation',methods=['GET','POST'])
def index():
    if request.method=='POST':
        location=request.form.get("fname1")
        db.child("SPOT").push(location)
        ns=request.form.get("fname2")
        db.child("SPOT").push(ns)
        cc=request.form.get("fname3")
        db.child("SPOT").push(cc)
        cp=request.form.get("fname4")
        db.child("SPOT").push(cp)
        linc=request.form.get("fname5")
        db.child("SPOT").push(linc)
        return render_template('6.html', fname1=location,fname2=ns,fname3=cc,fname4=cp,fname5=linc)
    else:
        return render_template('5.html')
    
@app.route('/login')
def login():
    return render_template('1.html')

@app.route('/userlogin')
def userlogin():
    return render_template('2.html')

@app.route('/hostlogin')
def hostlogin():
    return render_template('3.html')

@app.route('/ownedlocations')
def owned():
    return render_template('4.html')

@app.route('/updatedownedlocations')
def ownedupdated():
    return render_template('6.html')

@app.route('/parklocations')
def parklocations():
    cost=db.child('SPOT').get()
    co=cost.val()
    v=list(co.values())
    v[4]=str(v[4])
    return render_template('7.html',fname1=v[0],fname2=v[1],fname3=v[2],fname4=v[3],fname5=v[4])

@app.route('/parking')
def parking():
    return render_template('8.html')

@app.route('/wallet')
def wallet():
    return render_template('9.html')

@app.route('/redeem')
def redeem():
    return render_template('10.html')



@app.route('/publicspace')
def pp():
    return render_template('pp.html')

@app.route("/<fname1>")
def user(fname1):
    return f"<h1>{fname1}</h1>"

if __name__=="__main__":
    app.run(debug=False)