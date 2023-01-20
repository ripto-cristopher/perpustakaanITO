from application import app
from flask import jsonify, request, render_template
from application.models.transaksi.pengembalianModals import *
from application.controllers.auth import adminLoginRequired, session

@app.route('/transaksi/kembali/', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def pagePengembalian():
    return render_template("transaksi/pengembalian.html")


@app.route('/TransaksiPengembalian', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def TransaksiKembali():
    if request.method == 'GET':
        return "get"
    elif request.method == 'POST':
        idbuku = request.form['idbuku']
        denda = 0
        respon = insertKembalikan(idbuku, denda, session['id'])
       
        if respon['status'] == 'T':
            respon = updateSubBukuStatus(idbuku)
            respon = updatePinjam(idbuku)
            return "berhasi update sub buku status"
        return respon
    else:
        return "method tidak dapat dieksekusi"


