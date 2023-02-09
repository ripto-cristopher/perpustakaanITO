from application import app
from flask import jsonify, request, render_template, url_for, redirect, flash
from application.models.history.historyPeminjamanModals import *
from application.controllers.auth import adminLoginRequired


@app.route('/historypeminjaman', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def PageHistoryPeminjaman():
    data = getHistoryPengembalian()
    print (data)
    return render_template("history/historyPeminjaman.html", data=data)


# kembalikan ke/buka page history/historyPeminjaman.html dengan data=data
# {'status_code': 200, 'status': 'T', 'message': 'Sukses', 'result': [{'idbuku': 1, 'namabuku': 'Ubur-Ubur Lembur', 'nisanggota': 64945193,
#     'namaanggota': 'ABIMANYU MUHAMMAD RIYANDOKO', 'tanggalpeminjaman': datetime.date(2023, 2, 7), 'bataspengembalian': datetime.date(2023, 2, 9), 'flag': 0}]}
# 