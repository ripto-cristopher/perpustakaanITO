from application import app
from flask import jsonify, request, render_template, json
from application.controllers.auth import adminLoginRequired, session
from application.models.master.anggotaPerpustakaanModels import *
from application.models.transaksi.pengembalianModals import *


@app.route('/transaksi/bayar-denda')
@adminLoginRequired
def pageBayarDenda():

    return render_template("transaksi/bayarDenda.html")


def convert_to_int(currency_string):
    return int(currency_string.replace("Rp.", "").replace(".", ""))


@app.route('/transaksi-denda', methods=['POST'])
@adminLoginRequired
def transaksi_denda():
    id_anggota = request.form['idAnggotaPerpustakaan']
    nominal_bayar = convert_to_int(request.form['nominalBayar'])

    data_anggota = getAnggotaPerpustakaan(id_anggota)
    total_denda = data_anggota['result'][0]['totaldenda']
    denda_setelah_bayar = int(total_denda.replace(".", "").replace(",", "")) - nominal_bayar
    response = updateDendaAnggotaPerpustakaan(
        id_anggota, denda_setelah_bayar)

    if response['status'] == 'T':
        return jsonify({'message': 'Pembayaran berhasil'}), 200
    else:
        return jsonify({'message': 'Pembayaran gagal'}), 400