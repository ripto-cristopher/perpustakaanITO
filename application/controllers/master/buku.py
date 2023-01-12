from application import app
from flask import jsonify, request
from application.models.master.bukuModels import *
from application.controllers.auth import adminLoginRequired


@app.route('/master/buku', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def buku():
    if request.method == 'GET':
        data = getAllBuku()
        return jsonify(data)
    elif request.method == 'POST':
        idpenerbit = request.form['idpenerbit']
        idpengarang = request.form['idpengarang']
        idkategori = request.form['idkategori']
        nama = request.form['nama']
        tahunterbit = request.form['tahunterbit']
        respon = insertBuku(idpenerbit, idpengarang, idkategori, nama, tahunterbit)
        return respon
    elif request.method == 'PUT':
        id = request.form['id']
        idpenerbit = request.form['idpenerbit']
        idpengarang = request.form['idpengarang']
        idkategori = request.form['idkategori']
        nama = request.form['nama']
        tahunterbit = request.form['tahunterbit']
        respon = updateBuku(id, idpenerbit, idpengarang, idkategori, nama, tahunterbit)
        return respon
    else:
        return "method tidak dapat dieksekusi"


@app.route('/master/buku/sub/<int:id>', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def subBuku(id):
    if request.method == 'GET':
        print (id)
        print("subBuku")
        data = getAllsubBuku(id)
        return jsonify(data)
    elif request.method == 'POST':
        jumlah = request.form['jumlah']
        for n in range(int(jumlah)):
            respon = insertSubBuku(id)
            # buat array menampung new id dari sub buku yang baru dibuat
        return "berhasil memasukan sub buku"
    # elif request.method == 'PUT':
    #     id = request.form['id']
    #     idpenerbit = request.form['idpenerbit']
    #     idpengarang = request.form['idpengarang']
    #     idkategori = request.form['idkategori']
    #     nama = request.form['nama']
    #     tahunterbit = request.form['tahunterbit']
    #     respon = updateBuku(id, idpenerbit, idpengarang,
    #                         idkategori, nama, tahunterbit)
    #     return respon
    else:
        return "method tidak dapat dieksekusi"

