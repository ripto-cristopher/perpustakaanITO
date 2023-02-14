from application import app
from flask import jsonify, request, render_template, url_for, redirect, flash
from application.models.master.bukuModels import *
from application.controllers.auth import adminLoginRequired
from application.controllers.webservis import *
from application.controllers.master.buku import *



@app.route('/master/judulbuku', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def PageJudulBuku():
    all = {
        "penerbit": getAllpenerbit(),
        "pengarang": getAllpenulis(),
        "kategori": getAllKategori()
    }
    data = getAllJudulBuku()
    return render_template("master/judulBuku.html", all=all, data=data)


@app.route('/judulBuku/<int:id>/buku', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def bukuByJudulBuku(id):
    if request.method == 'GET':
        print(id)
        print("subBuku")
        data = getAllBukuByIdJudulBuku(id)
        return jsonify(data)
    elif request.method == 'POST':
        dict_id = {"result": []}
        buku = getJudulBuku(id)
        jumlah = request.form['jumlah']
        print(buku)
        '''
        dictionary menampung new id dari buku yang baru dibuat
        '''
        for n in range(int(jumlah)):
            respon = insertBuku(id)
            print(respon)
            dict_id["result"].append({
                "id_newSubBuku": respon['result'][0]['id'],
                "judul buku": buku['result'][0]['nama'],
                "kategori ": buku['result'][0]['kategori'],
                "penerbit ": buku['result'][0]['penerbit'],
                "tahunterbit ": buku['result'][0]['tahunterbit'],
                "pengarang ": buku['result'][0]['pengarang']
            })

        flash('buku berhasil ditambah ', 'success')
        # flash(dict_id, 'info')
        return redirect(url_for('PageJudulBuku'))
    else:
        return "method tidak dapat dieksekusi"

