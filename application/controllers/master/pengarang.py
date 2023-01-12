from application import app
from flask import jsonify, request
from application.models.master.pengarangModels import *
from application.controllers.auth import adminLoginRequired


@app.route('/master/penulis', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def pengarang():
    if request.method == 'GET':
        data = getAllpengarang()
        return jsonify(data)
    elif request.method == 'POST':
        nama = request.form['nama']
        re = insertpengarang(nama)
        return re
    elif request.method == 'PUT':
        id = request.form['id']
        nama = request.form['nama']
        re = updatepengarang(id, nama)
        return re
    else:
        return "method tidak dapat dieksekusi"
