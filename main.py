#from datetime import datetime  

from flask import Flask, render_template, redirect, request  

# Lib for SLQ Server
import pyodbc  

app = Flask(__name__)

def write(n,i):
    connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-CS9J9LQ;'
                      'Database=master;'
                      'Trusted_Connection=yes;')
    cursor = connection.cursor() 
    cursor.execute("INSERT INTO CUSTOMERS (ID, NAME) values ("+str(i)+",'"+ str(n)+"')")
    connection.commit()
    connection.close() 


# creating connection Object which will contain SQL Server Connection  
connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-CS9J9LQ;'
                      'Database=master;'
                      'Trusted_Connection=yes;')

# Creating Cursor   
cursor = connection.cursor()  
cursor.execute("SELECT * FROM CUSTOMERS")   
NAME=[]
ID =[]
for row in cursor:  
    NAME.append(row.NAME)
    ID.append(row.ID)
connection.close() 
cust={}

@app.route('/')  
@app.route('/home')
@app.route('/submit',methods = ["GET","POST"])
def home():
    if(request.method == "POST"):
        namex = request.form.get('namehtml')
        idx = request.form.get('idhtml')
        try:
            write(namex,idx)
        except:
            return render_template("error.html")
        NAME.append(namex)
        ID.append(idx)
        for i in range(len(NAME)):
            cust[NAME[i]]=ID[i] 
            
        return render_template("submit.html",result=cust , tot=len(NAME))
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=False)