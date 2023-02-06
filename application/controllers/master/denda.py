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
        "denda": getDenda(),
        "dendaActivate": getDendaActivate()['result'][0]['count']
    }

    print("page denda : data", data)
    return render_template("master/denda.html", data=data)


@app.route('/denda', methods=['POST'])
@adminLoginRequired
def denda():
    biayaDenda = request.form['biayaDenda']
    batasPeminjam = request.form['batasPeminjam']
    biayaDenda = int(biayaDenda[4:].replace(".", ""))
    print(biayaDenda, batasPeminjam)

    re = insertDenda(batasPeminjam, biayaDenda)
    if re['status'] == 'T':
        flash('denda berhasil disettings', 'success')
    else:
        flash('denda gagal disettings [001]', 'danger')
    return redirect(url_for('pageDenda'))


@app.route('/denda-update/', methods=['post'])
@adminLoginRequired
def dendaUpdate():
    id_denda = request.form['id_denda']
    statusDenda = getDendaById(id_denda)['result'][0]['activate']
    statusDenda = not statusDenda
    isDendaActivate = getDendaActivate()['result'][0]['count']
    print("isDendaActivate", statusDenda)
    if isDendaActivate != 0 and statusDenda != False:
        flash('denda masih yang ada yang aktif, silakan non-aktifkan terlebih dahulu', 'danger')
        return jsonify({'message': 'Update gagal', 'status': 'F'}), 200
    else:

        re = updateStatus(id_denda, statusDenda)

        if re['status'] == 'T':
            return jsonify({'message': 'Update gagal', 'status': 'T'}), 200
        else:
            return jsonify({'message': 'Update gagal'}), 400
