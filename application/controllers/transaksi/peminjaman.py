from application import app
from flask import jsonify, request, render_template
from application.models.transaksi.pinjamModels import *
from application.controllers.auth import adminLoginRequired, session


@app.route('/transaksi/pinjam')
@adminLoginRequired
def pagePinjam():
    return render_template("transaksi/peminjaman.html")


@app.route('/master/pinjam/<int:idAnggota>', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def pinjam(idAnggota):
    if request.method == 'GET':
        return "get"
        # return jsonify()
    elif request.method == 'POST':
        id = request.form['id']
        respon = insertPeminjaman(id, idAnggota, session['id'])
        print(id, idAnggota, session['id'])
        print(respon)
        if respon['status'] == 'T':
            respon = updateSubBukuStatus(id)
            return "berhasi update sub buku status"
        return respon
    else:
        return "method tidak dapat dieksekusi"
