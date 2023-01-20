from application import app
from functools import wraps
from flask import render_template, url_for, request, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from application.models.authmodels import *


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        reAdmin = selectAdmin(id)
        reUsers = selectUser(id)
        print(reUsers)
        if reAdmin['status'] == 'T' and reAdmin['result'] != []:
            if check_password_hash(reAdmin['result'][0]['password'], password):
                session['loggedin'] = True
                session['id'] = reAdmin['result'][0]['id']
                session['admin'] = True
                return redirect(url_for('home'))
                # return "anda berhasil login sebagai admin"
        elif reUsers['status'] == 'T' and reUsers['result'] != []:
            if check_password_hash(reUsers['result'][0]['password'], password):
                session['loggedin'] = True
                session['id'] = reUsers['result'][0]['id']
                session['email'] = reUsers['result'][0]['email']
                session['user'] = True
                return "anda berhasil login sebagai user"
        else:
            flash('wrong password or email', 'danger')
    return render_template("login.html")


@app.route('/register/admin', methods=['GET', 'POST'])
def registerAdmin():
    if request.method == 'POST':
        id = request.form['id']
        nama = request.form['nama']
        password = request.form['password']
        passwordHash = generate_password_hash(password, "sha256")
        print(passwordHash)
        re = insertAdmin(id, nama, passwordHash)
        if re['status'] == 'T':
            # flash('Registration has been successful, please login', 'success')
            # return redirect(url_for('login'))
            return re
        else:
            # flash('Registration failed', 'danger')
            # return "Registration gagal, danger"
            return re
    # return render_template("register.html")
    return f"berhasil {id}, {nama}, {passwordHash}"


@app.route('/register/user', methods=['GET', 'POST'])
def registerAnggota():
    if request.method == 'POST':
        id = request.form['id']
        nama = request.form['nama']
        email = request.form['email']
        kategori = request.form['kategori']
        tanggalLahir = request.form['tanggalLahir']
        print(tanggalLahir)
        passwordHash = generate_password_hash(tanggalLahir, "sha256")
        print(passwordHash)
        re = insertUser(id, nama.upper(), email.lower(),
                        tanggalLahir, kategori, passwordHash)
        if re['status'] == 'T':
            #     # flash('Registration has been successful, please login', 'success')
            #     # return redirect(url_for('login'))
            return re
        else:
            #     # flash('Registration failed', 'danger')
            #     # return "Registration gagal, danger"
            return re
    # return render_template("register.html")
    return f"berhasil {id}, {nama}, {passwordHash}"


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('admin', None)
    session.pop('id', None)
    # session.pop('nama', None)
    # session.pop('email', None)

    # session.pop('flag', None)  # 0 = admin | 1 = user
    return redirect(url_for('login'))


def adminLoginRequired(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print('loggedin' not in session)
        if 'loggedin' not in session and 'admin' not in session:
            # return "anda harus login terlebih dahulu"
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
