from flask import Flask, request, jsonify, Response
from flask_mysqldb import MySQL
from flask_cors import CORS
 
app = Flask(__name__)

#KONFIG KE DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'test_db'
app.config['JWT_SECRET_KEY']= "rahasia"

JWT_SECRET_KEY = 'rahasia'
 
mysql = MySQL(app)

# from blueprint_auth import authentication

# app.register_blueprint(authentication, url_prefix="/api/auth")

import jwt

def generate_jwt_token(content):
    encoded_content = jwt.encode(content, JWT_SECRET_KEY, algorithm="HS256")
    token = str(encoded_content)
    return token

def validate_user(email,password):
    cursor = mysql.connection.cursor()
    current_users = cursor.execute(''' SELECT * FROM users WHERE email=%s AND password_salt=%s''',(email,password))
    data = cursor.fetchone()
    print(current_users)
    if current_users == 1:
        user_id = data[0]
        jwt_token = generate_jwt_token({"id": user_id})
        return jwt_token
    else:
        return False

@app.route('/login', methods = ['POST', 'GET'])
def login_user():
    user_email = request.form["email"]
    user_password = request.form["password"]

    user_token = validate_user(user_email, user_password)

    if user_token:
        return jsonify({"jwt_token": user_token})
    else:
        Response(status=401)

app.run(host='localhost', port=5000)