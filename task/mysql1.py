from flask import Flask,request,jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host="localhost",user ="root",passwd="pass123")
cursor=mydb.cursor()
cursor.execute("create database if not exists tasksql")
cursor.execute("create table  if not exists tasksql.mysqltable(name varchar(30), number int)")

@app.route('/insert', methods=['GET','POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into tasksql.mysqltable values(%s , %s)", (name, number))
        mydb.commit()
        return jsonify(str('succesfully inserted'))
if __name__ == '__main__':
    app.run()