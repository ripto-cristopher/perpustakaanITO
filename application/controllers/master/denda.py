from application import app
from jinja2 import filters
from flask import jsonify, request, render_template, url_for, redirect, flash
from application.models.master.dendaModels import *
from application.controllers.auth import adminLoginRequired
from application.controllers.webservis import *

@app.route('/master/denda', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def pageDenda():

    data = {
        "denda" : getDenda(),
        "dendaActivate": getDendaActivate()['result'][0]['count']
    }
    return render_template("master/denda.html", data=data)


@app.route('/denda', methods=['POST'])
@adminLoginRequired
def denda():
    biayaDenda = request.form['biayaDenda']
    batasPeminjam = request.form['batasPeminjam']
    re = insertDenda(batasPeminjam, biayaDenda)
    if re['status'] == 'T':
        flash('denda berhasil disettings', 'success')
    else:
        flash('denda gagal disettings [001]', 'danger')
    return redirect(url_for('pageDenda'))


# {'status_code': 200, 'status': 'T', 'message': 'Sukses', 'result': [{'count': 0}]}