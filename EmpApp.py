from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'lab1'


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('twc.html')


@app.route("/about", methods=['POST'])
def about():
    return render_template('twc.html')


@app.route("/addemp", methods=['POST'])
def AddEmp():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    gender = request.form['gender']
    add = request.form['add']

    insert_sql = "INSERT INTO lab1 VALUES (%s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    try:

        cursor.execute(insert_sql, (name, email, phone, gender, add))
        db_conn.commit()

    finally:
        cursor.close()

    print("all modification done...")
    return render_template('twc.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

