from application import app
from flask import jsonify, render_template, request, flash, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from application.controllers.auth import usersLoginRequired
from application.models.master.bukuModels import *
from application.models.authmodels import *
from application.models.users.usersHomeModals import *


@app.route('/u', methods=['GET', 'POST'])
@usersLoginRequired
def usersHome():

    data = getAllJudulBuku()
    return render_template("users/usersHome.html", data=data)


@app.route('/u/change-password', methods=['GET', 'POST'])
@usersLoginRequired
def usersChangePassword():
    if request.method == 'POST':
        psw_sekarang = request.form['psw_sekarang']
        new_psw = request.form['new_psw']
        confirm_new_psw = request.form['confirm_new_psw']

        re = selectUser(session['id'])
        # re = selectUser(4)
        if check_password_hash(re['result'][0]['password'], psw_sekarang):
            if new_psw == confirm_new_psw:
                passwordHash = generate_password_hash(new_psw, "sha256")
                print(passwordHash)
                re = UpdatePswUsers(session['id'], passwordHash)
                print (re)
                flash('password berhasil diubah', 'success ')
                return redirect(url_for('usersHome'))
            else:
                flash('wrong confirm password ', 'danger')
    else:
        flash('wrong password', 'danger')
    return render_template("users/userChangePassword.html")


@app.route('/u/peminjaman', methods=['GET', 'POST'])
@usersLoginRequired
def usersPeminjaman():

    data = getPeminjamanUser(session['id'])
    return render_template("users/userPeminjaman.html", data=data)


