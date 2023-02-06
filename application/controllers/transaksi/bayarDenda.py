from application import app
from flask import jsonify, request, render_template, json
from application.models.transaksi.peminjamanModal import *
from application.controllers.auth import adminLoginRequired, session
from application.controllers.webservis import *
import datetime


@app.route('/transaksi/pinjam')
@adminLoginRequired
def pagePinjam():
    isdendaActivate = getDendaActivate()['result'][0]['count']
    if isdendaActivate == 0:
        flash('Belum ada Denda yang active silakan tambah denda', 'danger')
    return render_template("transaksi/peminjaman.html", isdendaActivate=isdendaActivate)


@app.route('/TransaksiPinjam', methods=['POST'])
@adminLoginRequired
def TransaksiPinjam():
    idAnggota = request.form['idAnggota']
    idBuku = json.loads(request.form['idBuku'])
    denda = getDenda()['result'][0]
    print(denda['lamapengembalian'])

    batasPengembalian = datetime.datetime.now().date(
    ) + datetime.timedelta(days=denda['lamapengembalian'])
    results = [insertPeminjaman(n, idAnggota, session['id'], denda['id'], batasPengembalian)
            for n in idBuku]
    print(results)
    status = all([r['status'] == 'T' for r in results])

    if status:
        [updateBukuStatus(n) for n in idBuku]
        return {'status': 'T', 'message': 'Transaksi peminjaman berhasil'}
    else:
        return {'status': 'F', 'message': 'Terjadi kesalahan saat melakukan transaksi peminjaman'}


    





