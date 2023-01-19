from application import app
from flask import jsonify, request, render_template, url_for, redirect, flash
from application.models.master.bukuModels import *
from application.controllers.auth import adminLoginRequired
from application.controllers.webservis import *


@app.route('/master/buku', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def buku():
    data = getAllBuku()
    all = {
        "penerbit": getAllpenerbit(),
        "pengarang": getAllpenulis(),
        "kategori": getAllKategori()
    }
    print(data)

    if request.method == 'POST':
        nama = request.form['judul_buku']
        idpenerbit = request.form['select_penerbit']
        idpengarang = request.form['select_pengarang']
        idkategori = request.form['select_kategori']
        tahunterbit = request.form['tahunterbit']
        respon = insertBuku(idpenerbit, idpengarang,
                            idkategori, nama, tahunterbit)
        flash('buku berhasil ditambah ', 'success')

        return redirect(url_for('buku'))
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

    return render_template("master/buku.html", data=data, all=all)


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
        print(buku)
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
        flash('buku berhasil ditambah ', 'success')
        flash(dict_id, 'info')
        return redirect(url_for('buku'))
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
