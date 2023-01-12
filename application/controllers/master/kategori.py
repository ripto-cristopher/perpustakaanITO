from application import app
from flask import jsonify, request
from application.models.master.kategoriModels import *
from application.controllers.auth import adminLoginRequired


@app.route('/master/kategori', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def kategori():
    if request.method == 'GET':
        data = getAllKategori()
        return jsonify(data)
    elif request.method == 'POST':
        nama = request.form['nama']
        re = insertKategori(nama)
        return re
    elif request.method == 'PUT':
        id = request.form['id']
        nama = request.form['nama']
        re = updateKategori(id, nama)
        return re
    else :
        return "method tidak dapat dieksekusi" 



