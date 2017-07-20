import sqlite3 as sql
import request
from flask import Flask,render_template
app = Flask(__name__)


@app.route('/enternew')
def new_student():
   return render_template('friendshome.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['name']
            email=request.form['email']
            comm=request.form['comments']
            with sql.connect("mywebsite.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO CONTACTINFO(nm,email,comm) VALUES(?,?,?)",(nm,email,comm))
                con.commit()
                msg="Record successfully added"
                return msg
        except:
            con.rollback()
            msg="sorry database problem"
        finally:
            return render_template("friendshome.html",msg=msg)
            con.close()

