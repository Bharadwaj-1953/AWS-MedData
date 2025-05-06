
from flask import request,Flask,render_template,session,redirect,url_for,flash
import pymysql
import pandas as pd


app=Flask(__name__)
app.config['SECRET_KEY']='f9bf78b9a18ce6d46a0cd2b0b86df9da'

db = pymysql.connect(host='localhost',user='root',password='',db='multisource',port=3306)
cursor=db.cursor()

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/admin",methods=["POST","GET"])
def admin():
    if request.method=="POST":
        name=request.form["name"]
        pwd=request.form["pwd"]
        if name=="admin" and pwd=="admin":
            return render_template("adminhome.html",msg="success")
    return render_template("admin.html")

@app.route("/viewdoctors")
def viewdoctors():
    sql="select * from doctor"
    data=pd.read_sql_query(sql,db)
    data["Action"]="Action"
    data.drop(["email","pwd","cpwd","gender","mobile"],inplace=True,axis=1)
    return render_template("viewdoctors.html",row_val=data.values.tolist(), msg="success" )

@app.route("/adddoct/<s1>/<s2>/<s3>")
def adddoct(s1="",s2="",s3=""):
    return render_template("adddoctors.html",s1=s1,s2=s2,s3=s3,msg="success")

@app.route("/updoctors",methods=["POST","GET"])
def updoctors():
    if request.method=="POST":
        name=request.form["name"]
        age=request.form["age"]
        role=request.form["role"]
        sql = "insert into addoctors (name,age,role) values (%s,%s,%s)"
        values = (name,age,role)
        cursor.execute(sql, values)
        db.commit()
        flash("Doctor Added successfully","success")
        return redirect(url_for('viewdoctors'))


@app.route("/viewpatients")
def viewpatients():
    sql = "select * from patient"
    data = pd.read_sql_query(sql, db)
    data.drop(["email","pwd","cpwd","gender","mobile"],inplace=True,axis=1)
    data["Action"]="Action"
    return render_template("viewpatients.html",row_val=data.values.tolist(), msg="success")

@app.route("/addpatients/<s1>/<s2>/<s3>")
def addpatients(s1="",s2="",s3=""):
    return render_template("addpat.html",s1=s1,s2=s2,s3=s3, msg="success")
@app.route("/uppat",methods=["POST","GET"])
def uppat():
    if request.method=="POST":
        name=request.form["name"]
        age=request.form["age"]
        disease=request.form["disease"]
        sql = "insert into adpatients (name,age,disease) values (%s,%s,%s)"
        values = (name, age, disease)
        cursor.execute(sql, values)
        db.commit()
        flash("Patient added successfully ","success")
        return redirect(url_for('viewpatients'))
        

@app.route("/viewmedicines")
def viewmedicines():
    sql="select * from filesupload"
    data = pd.read_sql_query(sql, db)
    data.drop(["requeststofiles"],axis=1,inplace=True)
    data["Action"]="Action"
    return render_template("viewmedicines.html",row_val=data.values.tolist())

@app.route(("/addreqtoioh/<s1>"))
def addreqtoioh(s1=0):
    sql="update filesupload set requeststofiles='%s' where sno='%s' "%("pending",s1)
    cursor.execute(sql)
    db.commit()
    flash("Request sended successfully To IOH","success")
    return redirect(url_for('viewmedicines'))

@app.route("/viewses")
def viewses():
    sql="select * from filesupload where requeststofiles='accepted'"
    data=pd.read_sql_query(sql,db)
    data["Action"]="Action"
    return render_template("viewses.html",row_val=data.values.tolist())


@app.route("/key/<s1>")
def key(s1=0):
    sql = "select count(*),AES_DECRYPT(files,'rupesh') from filesupload where sno='%s' " % (s1)
    x=pd.read_sql_query(sql,db)
    count=x.values[0][0]
    if count==0:
        flash("Invalid Key","success")
    else:
        data=x.values[0][1]
        print(data)
        data=data.decode('utf-8')
    # cursor.execute(sql)
    # data = pd.read_sql_query(sql, db)
        return render_template("key.html", row_val=data)
    return redirect(url_for('viewses'))

@app.route("/viewdocses")
def viewdocses():
    sql="select * from filesupload where requeststofiles='accepted'"
    data=pd.read_sql_query(sql,db)
    data["Action"]="Action"
    return render_template("viewdocses.html",row_val=data.values.tolist())

@app.route("/key1/<s1>")
def key1(s1=0):
    sql = "select count(*),AES_DECRYPT(files,'rupesh') from filesupload where sno='%s' " % (s1)
    x=pd.read_sql_query(sql,db)
    count=x.values[0][0]
    if count==0:
        flash("Invalid Key","success")
    else:
        data=x.values[0][1]
        print(data)
        data=data.decode('utf-8')
    # cursor.execute(sql)
    # data = pd.read_sql_query(sql, db)
        return render_template("key1.html", row_val=data)
    return redirect(url_for('viewdocses'))

@app.route("/viewpatses")
def viewpatses():
    sql="select * from filesupload where requeststofiles='accepted'"
    data=pd.read_sql_query(sql,db)
    data["Action"]="Action"
    return render_template("viewpatses.html",row_val=data.values.tolist())

@app.route("/key2/<s1>")
def key2(s1=0):
    sql = "select count(*),AES_DECRYPT(files,'rupesh') from filesupload where sno='%s' " % (s1)
    x=pd.read_sql_query(sql,db)
    count=x.values[0][0]
    if count==0:
        flash("Invalid Key","success")
    else:
        data=x.values[0][1]
        print(data)
        data=data.decode('utf-8')
    # cursor.execute(sql)
    # data = pd.read_sql_query(sql, db)
        return render_template("key2.html", row_val=data)
    return redirect(url_for('viewpatses'))

@app.route("/doctor",methods=["POST","GET"])
def doctor():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        age = request.form["age"]
        pwd=request.form["pwd"]
        cpwd=request.form["pwd"]
        gender=request.form["gender"]
        mobile=request.form["mobile"]
        role=request.form["role"]
        sql = "insert into doctor (name,email,age,pwd,cpwd,gender,mobile,role) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (name,email,age,pwd,cpwd,gender,mobile,role)
        cursor.execute(sql, values)
        db.commit()
        return render_template("doctor.html",ms="success")
    return render_template("doctor.html")

@app.route("/doctorlogin",methods=['POST','GET'])
def doctorlogin():
    if request.method=='POST':
        name = request.form["name"]
        pwd = request.form["pwd"]
        sql="select * from doctor where name=%s and pwd=%s "
        val=(name,pwd)
        X=cursor.execute(sql,val)
        Results=cursor.fetchall()
        if X>0:

            session["doctorloginid"]=Results[0][0]
            session["doctorname"]=Results[0][1]

            return render_template("doctorshome.html",msg="sucess")
        else:
            print("5555555555555")
            return render_template("doctorlogin.html",mfg="not found")
    return render_template("doctorlogin.html")


@app.route("/viewappointments")
def viewappointments():
    print(session["doctorloginid"])
    sql="select * from addrequesttodoctor where doctorid=%s"%(session["doctorloginid"])
    data=pd.read_sql_query(sql,db)
    print(data)
    session["s1"]=data.values[0][0]
    data.drop(["appointmentdate","status","doctorname"],axis=1,inplace=True)
    data["Action"]="Action"
    return render_template("viewappointments.html",row_val=data.values.tolist())

@app.route("/addappointment",methods=["POST","GET"])
def addappointment():
    if request.method=="POST":
        date1=request.form["date"]
        from datetime import datetime
        now = datetime.now()
        currentDay = datetime.now().strftime('%Y-%m-%d')
        print(date1)
        print(currentDay)
        if date1 > currentDay:
            sql = "update  addrequesttodoctor set appointmentdate='%s',status='%s',doctorname='%s' where sno='%s'" %(date1,"accepted",session["doctorname"],session["s1"])
            cursor.execute(sql)
            db.commit()
            flash("Appointment comfirmed","success")
            return redirect(url_for('viewappointments'))
        else:
            flash("Select future date","danger")
            return  redirect('viewappointments')
    return render_template("addappointment.html")

@app.route("/patient",methods=["POST","GET"])
def patient():
    if request.method=="POST":
        name = request.form["name"]
        email = request.form["email"]
        pwd = request.form["pwd"]
        cpwd = request.form["pwd"]
        age = request.form["age"]
        gender = request.form["gender"]
        mobile = request.form["mobile"]
        dissease = request.form["disease"]
        if pwd==cpwd:
            sql = "insert into patient (name,email,age,pwd,cpwd,gender,mobile,disease) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (name, email,age, pwd, cpwd, gender, mobile, dissease)
            cursor.execute(sql, values)
            db.commit()
            return render_template("patient.html", ms="success")
        else:
            return render_template("patient.html", m1s="fg")
    return render_template("patient.html")

@app.route("/patientlogin",methods=['POST','GET'])
def patientlogin():
    if request.method=='POST':
        name = request.form["name"]
        pwd = request.form["pwd"]
        sql="select * from patient where name=%s and pwd=%s "
        val=(name,pwd)
        X=cursor.execute(sql,val)
        Results=cursor.fetchall()
        if X>0:
            session["patientdisease"]=Results[0][8]
            print(session["patientdisease"])
            session["patientname"]=Results[0][1]
            session["patientage"]=Results[0][3]
            session["patientid"]=Results[0][0]
            return render_template("patienthome.html",msg="sucess")
        else:

            return render_template("patientlogin.html",mfg="not found")
    return render_template("patientlogin.html")
@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/searchback",methods=['POST','GET'])
def searchback():
    print("dfhlksokhso")
    if request.method == 'POST':
        dtype = request.form['dtype']
        sql = "select * from addoctors where role LIke '%"+dtype+"%' "
        x=pd.read_sql_query(sql,db)
        # args = [ dtype + '%']
        # cursor.execute(sql, db)
        # data = pd.DataFrame(cursor.fetchall())
        # print(data)
        x["Action"] = "Action"
        return render_template("viewaddoctors.html", row_val=x.values.tolist())

@app.route("/viewaddoctors")
def viewaddoctors():
    # session["patientdisease"]="card"
    sql = 'SELECT * FROM addoctors WHERE role LIKE %s'
    args = [ session["patientdisease"] + '%']
    cursor.execute(sql, args)
    data = pd.DataFrame(cursor.fetchall())
    print(data)
    data["Action"]="Action"
    flash("Appointment Sended ","success")
    return render_template("viewaddoctors.html",row_val=data.values.tolist(), msg="added")

@app.route("/addrequesttodoctor/<s1>/<s2>")
def addrequesttodoctor(s1=0,s2=""):
    d=session.get('patientdisease')
    print(d)
    sql = "insert into addrequesttodoctor (name,age,disease,doctorid,doctorsname, patientid) values (%s,%s,%s,%s,%s,%s)"
    values = (session["patientname"],session["patientage"], d, session["patientid"],s2, s1 )
    cursor.execute(sql, values)
    db.commit()
    return redirect(url_for('viewaddoctors'))

@app.route("/viewstatus")
def viewstatus():
    sql = "select * from addrequesttodoctor where status='%s' "%("accepted")
    data=pd.read_sql_query(sql,db)
    data.drop(["disease","patientid","age","doctorname","doctorid","sno"],axis=1,inplace=True)
    return render_template("viewstatus.html",row_val=data.values.tolist())

@app.route("/ioh",methods=["POST","GET"])
def ioh():
    if request.method == "POST":
        name = request.form["name"]
        pwd = request.form["pwd"]
        if name == "IOH" and pwd == "IOH":
            return render_template("iohhome.html", msg="success")
    return render_template("ioh.html")

@app.route("/iohviewpatients")
def iohviewpatients():
    sql="select * from addrequesttodoctor"
    data=pd.read_sql_query(sql,db)
    data.drop(["patientid","doctorid","doctorname"],axis=1,inplace=True)
    return render_template("iohviewpatients.html",row_val=data.values.tolist())

@app.route("/uploadmedicienes", methods=["POST", "GET"])
def uploadmedicienes():
    sql = "select * from addrequesttodoctor"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    name = data[0][1]
    age = data[0][2]
    disease = data[0][3]
    doctorsname = data[0][5]
    print(name, age, disease, doctorsname)

    if request.method == "POST":
        fname = request.form["fname"]
        files = request.form["files"]
        dd = r"uploadfiles/" + files
        with open(dd, "r") as f:
            file_data = f.read()
        print(file_data)

        sql = "INSERT INTO filesupload (name, age, disease, doctorsname, fname, files) VALUES (%s, %s, %s, %s, %s, AES_ENCRYPT(%s, 'rupesh'))"
        values = (name, age, disease, doctorsname, fname, file_data)
        
        cursor.execute(sql, values)
        db.commit()
        flash("Data Uploaded Successfully", "success")

    return render_template("uploadmedicienes.html")

@app.route("/viewadminrequests")
def viewadminrequests():
    return render_template("viewadminrequests.html")


@app.route("/Viewre")
def Viewre():
    sql="select * from filesupload where requeststofiles='%s'"%("pending")
    data=pd.read_sql_query(sql,db)
    data.drop(["files"],axis=1,inplace=True)
    # data["age"]="age"
    return render_template("Viewre.html",row_val=data.values.tolist())

@app.route("/upd/<s1>")
def upd(s1=0):
    sql="update filesupload set requeststofiles='%s' where sno='%s' "%("accepted",s1)
    cursor.execute(sql)
    db.commit()
    flash("File Request Accepted Successfully","success")
    return redirect(url_for('viewadminrequests'))

if(__name__)==("__main__"):
    app.secret_key = 'f9bf78b9a18ce6d46a0cd2b0b86df9da'

    app.run(debug=True)