from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
 
app = Flask(__name__)

#KONFIG KE DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'test_db'
 
mysql = MySQL(app)

#API FLASK
@app.route('/test', methods = ['POST', 'GET'])
def index():
    
    if request.method == 'GET':
        api_key = request.headers['api_key'] 
        if api_key == 'secret': 
            cursor = mysql.connection.cursor()
            return "Data Production"
        else:
            return "Don't forget enter the key"
     
    if request.method == 'POST':
        print(request.form)
        id_cluster = request.form['id_cluster']
        cluster = request.form['cluster']
        id_sub_cluster = request.form['id_sub_cluster']
        sub_cluster = request.form['sub_cluster']
        channel = request.form['channel']
        b_realitation = request.form['b_realitation']
        b_domestik = request.form['b_domestik']
        periode = request.form['periode']
        id_member = request.form['id_member']
        member_name = request.form['member_name']
        dectotal = request.form['dectotal']
        id_sub_class_component = request.form['id_sub_class_component']
        sub_class_component = request.form['sub_class_component']
        measurement_type = request.form['measurement_type']
        remark = request.form['remark']
        py = request.form['py']
        pq = request.form['pq']
        pm = request.form['pm']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO production VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(id_cluster,cluster,id_sub_cluster,sub_cluster,channel,b_realitation,b_domestik,periode,id_member,member_name,dectotal,id_sub_class_component,sub_class_component,measurement_type,remark,py,pq,pm))
        mysql.connection.commit()
        cursor.close()
        return jsonify( message= "Success", statusCode= 200)

@app.route('/test/<id>', methods = ['POST', 'GET','PUT','DELETE'])
def get_byId(id):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM production WHERE id_cluster=%s ''',(id,))
        data = cursor.fetchone()
        # dict_data = {'id_cluster':data[0],'cluster':data[1]}
        # data1 = { 'id' : data[0], 'name' :data[1], 'alamat' : data[2]}
        # return jsonify(isError= False, message= "Success", statusCode= 200, data= data), 200
        return jsonify(data = data,isError= False, message= "Success", statusCode= 200 ), 200
    if request.method == 'DELETE':
        cursor = mysql.connection.cursor()
        data = cursor.execute('''DELETE FROM users WHERE id = (%s)''',(id))
        mysql.connection.commit()
        cursor.close()
        return jsonify( message= "Success", statusCode= 200, data =data)
 
app.run(host='localhost', port=5000)