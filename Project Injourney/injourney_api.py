from flask import Flask, request, jsonify
 
app = Flask(__name__)

#KONFIG KE DB
import singlestoredb as s2
conn = s2.connect('svc-3479b32e-b09c-4933-a069-d151ce16a097-dml.gcp-jakarta-1.svc.singlestore.com:3306/AVIATA_CRP_DASHBOARD', user='admin', password='Aviata2022*',local_infile=True)

#API FLASK
@app.route('/production', methods = ['POST', 'GET'])
def index():
    
    if request.method == 'GET':
        api_key = request.headers['api_key'] 
        if api_key == 'secret': 
            cursor = conn.cursor()
            return "Data Production"
        else:
            return "Don't forget enter the key"
     
    if request.method == 'POST':
        print(request.json)
        id_cluster = request.json['id_cluster']
        cluster = request.json['cluster']
        id_sub_cluster = request.json['id_sub_cluster']
        sub_cluster = request.json['sub_cluster']
        channel = request.json['channel']
        b_realitation = request.json['b_realitation']
        b_domestik = request.json['b_domestik']
        periode = request.json['periode']
        id_member = request.json['id_member']
        member_name = request.json['member_name']
        dectotal = request.json['dectotal']
        id_sub_class_component = request.json['id_sub_class_component']
        sub_class_component = request.json['sub_class_component']
        measurement_type = request.json['measurement_type']
        remark = request.json['remark']
        py = request.json['py']
        pq = request.json['pq']
        pm = request.json['pm']
        cursor = conn.cursor()
        cursor.execute(''' INSERT INTO production VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(id_cluster,cluster,id_sub_cluster,sub_cluster,channel,b_realitation,b_domestik,periode,id_member,member_name,dectotal,id_sub_class_component,sub_class_component,measurement_type,remark,py,pq,pm))
        conn.commit()
        cursor.close()
        return jsonify( message= "Success", statusCode= 200)

@app.route('/production/<id>', methods = ['POST', 'GET','PUT','DELETE'])
def get_byId(id):
    if request.method == 'GET':
        cursor = conn.cursor()
        cursor.execute(''' SELECT * FROM production WHERE id_cluster=%s ''',(id,))
        data = cursor.fetchone()
        return jsonify(data = data,isError= False, message= "Success", statusCode= 200 ), 200
    if request.method == 'DELETE':
        cursor = conn.cursor()
        data = cursor.execute('''DELETE FROM users WHERE id = (%s)''',(id))
        conn.connection.commit()
        cursor.close()
        return jsonify( message= "Success", statusCode= 200, data =data)
 
app.run(host='0.0.0.0')
