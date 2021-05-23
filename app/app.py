#coding: utf-8

from flask import Flask, render_template, redirect, url_for, request

from mysql.connector import (connection)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
    
@app.route("/hi")
def hi():
    str = "Hi. This is Python rest service"
    return str
    
'''@app.route("/getcustomers")
def getcustomers():
    cnx = mysql.connector.connect(user='root', password='dsouza',host='127.0.0.1',database='_test')
    
    cursor = cnx.cursor()

    query = ("SELECT * from _mytable")

    cursor.execute(query)

    for (_id, _mynumber, _myname,_mydate,_mystring) in cursor:
      print("ID = {}, Number={}, Name={} ,Date = {}, String={} {:%d %s %s %s %s}".format(_id, _mynumber, _myname,_mydate,_mystring))

    cursor.close()
    cnx.close()
    return
'''


@app.route("/getcustomer")
def getCustomer():
    if request.method == 'GET':
        name = request.args.get('name')
        email = request.args.get('email')
        phone = request.args.get('phone')
        feedback = request.args.get('feedback')
        print("name=",name," ","email=",email,"phone=",phone,"feedback=",feedback)
        query = "insert into customer (name,email,phone,feedback) values (" + "'" + name + "'" + "," + "'" + email+ "'" + "," + "'" + phone + "'" +"," + "'" + feedback+ "'" +")"
        print ("query=",query)
        executequery(query)
        return "query fired successfully"
        
def executequery(query):
    print ("firing a query")
    cnx = connection.MySQLConnection(user='root', password='mysql',host='localhost',database='customers')
    
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()
    
    cnx.close()
    print ("query fired  successfully")
    return 
        

'''        
@app.route("/getcustomers2")
def getcustomers2():
    cnx = connection.MySQLConnection(user='root', password='mysql',host='localhost',database='customers')
    
    cursor = cnx.cursor()

    query = ("SELECT * from customer")

    cursor.execute(query)

    for (id, name,email,phone,feedback) in cursor:
      print("id =", id, "name=", name,"email=", email, "phone=",phone,"feedback=",feedback)

    cursor.close()
    
    cnx.close()
    
    return "getcustomer2 called successfully"  '''
  
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
