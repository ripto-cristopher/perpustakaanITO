from application import app
from flask import jsonify, request, render_template, flash, redirect, url_for
from application.models.master.kategoriModels import *
from application.controllers.auth import adminLoginRequired


@app.route('/master/kategori', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def kategori():
    data = getAllKategori()
    if request.method == 'POST':
        nama = request.form['nama']
        re = insertKategori(nama)
        flash('kategori '+nama+' berhasil ditambah ', 'success')

        return redirect(url_for('kategori'))
    elif request.method == 'PUT':
        id = request.form['id']
        nama = request.form['nama']
        re = updateKategori(id, nama)
        return re
     
    return render_template("master/kategori.html", data=data)



