from flask import Flask,render_template,Response,request,redirect,url_for

app=Flask(__name__)



@app.route('/newlocation',methods=['GET','POST'])
def index():
    if request.method=='POST':
        location=request.form.get("fname1")
        ns=request.form.get("fname2")
        cc=request.form.get("fname3")
        cp=request.form.get("fname4")
        linc=request.form.get("fname5")
        locationdata=[location,ns,cc,cp,linc]
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
    return render_template('7.html')

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