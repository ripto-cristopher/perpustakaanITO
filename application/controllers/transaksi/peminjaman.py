from application import app
from flask import jsonify, request, render_template, json
from application.models.transaksi.peminjamanModal import *
from application.controllers.auth import adminLoginRequired, session
from application.controllers.webservis import *

@app.route('/transaksi/pinjam')
@adminLoginRequired
def pagePinjam():
    return render_template("transaksi/peminjaman.html")


@app.route('/TransaksiPinjam', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def TransaksiPinjam():
    if request.method == 'POST':
        idAnggota = request.form['idAnggota']
        idBuku = json.loads(request.form['idBuku'])
        for n in idBuku :
            respon = insertPeminjaman(n, idAnggota, session['id'])
            print(idBuku, idAnggota, session['id'])
            print(respon)
            if respon['status'] == 'T':
                respon = updateBukuStatus(n)
                print("respon  ", respon)
                return respon
    else:
        return "method tidak dapat dieksekusi"


