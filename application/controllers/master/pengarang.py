from application import app
from flask import jsonify, request, render_template, redirect, url_for, flash
from application.models.master.penulisModels import *
from application.controllers.auth import adminLoginRequired


@app.route('/master/penulis', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def penulis():
    data = getAllpenulis()
    if request.method == 'POST':
        nama = request.form['nama']
        re = insertpenulis(nama)
        flash('Penulis '+nama+' berhasil ditambah ', 'success')
        return redirect(url_for('penulis'))
    elif request.method == 'PUT':
        id = request.form['id']
        nama = request.form['nama']
        re = updatepenulis(id, nama)
        return re
    return render_template("master/penulis.html", data=data)
