from application import app
from flask import jsonify, request, render_template, flash, redirect, url_for
from application.models.master.penerbitModels import *
from application.controllers.auth import adminLoginRequired


@app.route('/master/penerbit', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def penerbit():
    data = getAllpenerbit()
    if request.method == 'POST':
        nama = request.form['nama']
        re = insertpenerbit(nama)
        flash('kategori '+nama+' berhasil ditambah ', 'success')
        return redirect(url_for('penerbit'))

    elif request.method == 'PUT':
        id = request.form['id']
        nama = request.form['nama']
        re = updatepenerbit(id, nama)
        return re

    return render_template("master/penerbit.html", data=data)
