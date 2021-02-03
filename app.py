#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess
from flask import Flask, jsonify, request, render_template
import pymysql
from datetime import datetime

db = pymysql.connect(
    user='dbuser', 
    passwd='abcd1234', 
    host='127.0.0.1', 
    db='study', 
    charset='utf8'
) 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/chatlist', methods=['GET'])
def modellist():
    data = request.args.to_dict()
    # data = request.get_json()
    print(data)
    lastno = data['lastno']
    
    cursor = db.cursor(pymysql.cursors.DictCursor)
    if lastno == '0' :
        sql = 'SELECT MAX(no) AS lastno FROM chat;'
        cursor.execute(sql)
        lastno = str(cursor.fetchone()['lastno'])
        if lastno == 'None':
            lastno = '0'

    sql = 'SELECT * FROM chat WHERE no > ' + lastno +';'
    cursor.execute(sql)
    chatlist = cursor.fetchall()
    lastno = str(int(lastno) + len(chatlist))

    return jsonify(result = "success", result2 = chatlist, lastno = lastno)

if __name__ == '__main__':
    # try:
    #     parser = argparse.ArgumentParser(descrㄹiption="")
    #     parser.add_argument('--listen-port',  type=str, required=True, help='REST service listen port')
    #     args = parser.parse_args()
    #     listen_port = args.listen_port
    # except Exception as e:
    #     print('Error: %s' % str(e))

    #TODO bctak: Need to select one IP that is externally visible. Currently, it just picks the first one.
    listen_port = '4000'

    ipaddr=subprocess.getoutput("hostname -I").split()[0]
    print ("Starting the service with ip_addr="+ipaddr)
    app.run(debug=True,host=ipaddr,port=int(listen_port),threaded=True)
