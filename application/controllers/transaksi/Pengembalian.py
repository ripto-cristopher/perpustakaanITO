from application import app
from flask import jsonify, request, render_template
from application.models.transaksi.pengembalianModals import *
from application.controllers.auth import adminLoginRequired, session
import datetime


@app.route('/transaksi/kembali/', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def pagePengembalian():
    return render_template("transaksi/pengembalian.html")


# @app.route('/TransaksiPengembalian', methods=['POST'])
# @adminLoginRequired
# def TransaksiKembali():
#     if request.method == 'POST':
#         idbuku = request.form['idbuku']
#         # print(getpeminjaman(idbuku))
#         pengembalian = getpeminjaman(idbuku)['result'][0]

#         denda = 0
#         if pengembalian['bataspengembalian'] < datetime.datetime.now().date():
#             denda = (datetime.datetime.now().date() - pengembalian['bataspengembalian']).days * pengembalian['besardenda']
#         insertKembalikan(idbuku, denda, session['id'], pengembalian['id'])
#         updateSubBukuStatus(idbuku)
#         updatePinjam(idbuku)
#         return "berhasil update sub buku status"
#     return "method tidak dapat dieksekusi"


@app.route('/TransaksiPengembalian', methods=['POST'])
@adminLoginRequired
def TransaksiKembali():
    if request.method == 'POST':
        idbuku = request.form['idbuku']
        pengembalian = getpeminjaman(idbuku)['result'][0]
        batasPengembaian = datetime.date(2023, 2, 13)
        totalDenda = getTotalDendaAnggotaPerpustakaan(
            pengembalian['idanggotaperpustakaan'])['result'][0]['totaldenda']
        print("totalDenda \n", totalDenda)
        denda = 0
        if pengembalian['bataspengembalian'] < batasPengembaian:
            denda = (batasPengembaian -
                     pengembalian['bataspengembalian']).days * pengembalian['besardenda']
            print("denda, pengembalian['besardenda'], (batasPengembaian - pengembalian['bataspengembalian']).days\n",
                  denda, pengembalian['besardenda'], (batasPengembaian - pengembalian['bataspengembalian']).days)
        res = insertKembalikan(
            idbuku, denda, session['id'], pengembalian['id'])
        print(res)
        if res['status'] == 'T':
            totalDenda = int(totalDenda or 0) + denda
            res = updateDendaAnggotaPerpustakaan(
                pengembalian['idanggotaperpustakaan'], totalDenda)
            print (res)
            updateSubBukuStatus(idbuku)
            updatePinjam(idbuku)

        return "berhasil update sub buku status"
    return "method tidak dapat dieksekusi"
