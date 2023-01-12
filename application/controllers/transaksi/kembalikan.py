from application import app
from flask import jsonify, request
from application.models.transaksi.kembalikanModels import *
from application.controllers.auth import adminLoginRequired, session

@app.route('/transaksi/kembali/', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def kembali():
    if request.method == 'GET':
        return "get"
        # return jsonify()
    elif request.method == 'POST':
        idSubBuku = request.form['idSubBuku']
        denda = 0
        respon = insertKembalikan(idSubBuku, denda, session['id'])
       
        if respon['status'] == 'T':
            respon = updateSubBukuStatus(idSubBuku)
            respon = updatePinjam(idSubBuku)
            return "berhasi update sub buku status"
        return respon
    else:
        return "method tidak dapat dieksekusi"

