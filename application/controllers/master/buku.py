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
        respon = insertBuku(idpenerbit, idpengarang,
                            idkategori, nama, tahunterbit)
        return respon
    elif request.method == 'PUT':
        id = request.form['id']
        idpenerbit = request.form['idpenerbit']
        idpengarang = request.form['idpengarang']
        idkategori = request.form['idkategori']
        nama = request.form['nama']
        tahunterbit = request.form['tahunterbit']
        respon = updateBuku(id, idpenerbit, idpengarang,
                            idkategori, nama, tahunterbit)
        return respon
    else:
        return "method tidak dapat dieksekusi"


@app.route('/master/buku/<int:id>/sub', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def subBuku(id):
    if request.method == 'GET':
        print(id)
        print("subBuku")
        data = getAllsubBuku(id)
        return jsonify(data)
    elif request.method == 'POST':
        dict_id = {"result": []}
        buku = getBuku(id)
        jumlah = request.form['jumlah']
        print (buku)
        for n in range(int(jumlah)):
            respon = insertSubBuku(id)
            dict_id["result"].append({
                "id_newSubBuku": respon['result'][0]['id'],
                "judul buku": buku['result'][0]['nama'],
                "kategori ": buku['result'][0]['kategori'],
                "penerbit ": buku['result'][0]['penerbit'],
                "tahunterbit ": buku['result'][0]['tahunterbit'],
                "pengarang ": buku['result'][0]['pengarang']
            })
            # buat array menampung new id dari sub buku yang baru dibuat
        return jsonify(dict_id)
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
