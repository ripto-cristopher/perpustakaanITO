from application import app
from flask import jsonify, request
from application.models.master.penerbitModels import *
from application.controllers.auth import adminLoginRequired


@app.route('/master/penerbit', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def penerbit():
    if request.method == 'GET':
        data = getAllpenerbit()
        return jsonify(data)
    elif request.method == 'POST':
        nama = request.form['nama']
        re = insertpenerbit(nama)
        return re
    elif request.method == 'PUT':
        id = request.form['id']
        nama = request.form['nama']
        re = updatepenerbit(id, nama)
        return re
    else:
        return "method tidak dapat dieksekusi"
