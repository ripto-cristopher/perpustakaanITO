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
            else:
                flash('wrong password or nisn', 'danger')
        if reUsers['status'] == 'T' and reUsers['result'] != []:
            if check_password_hash(reUsers['result'][0]['password'], password):
                session['loggedin'] = True
                session['id'] = reUsers['result'][0]['id']
                session['user'] = True
                return redirect(url_for('usersHome'))
            else:
                flash('wrong password or nisn', 'danger')
        else:
            flash('wrong password or nis', 'danger')
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
        print(re)
        if re['status'] == 'T':
            flash('anggota perpustakaan '+nama +
                  ' berhasil ditambah ', 'success')

            return redirect(url_for('pageAnggotaPerpustakaan'))
        else:
            flash(
                'anggota perpustakaan gagal ditambahakan nisn/email duplikat ', 'danger')
            #     # flash('Registration failed', 'danger')
            #     # return "Registration gagal, danger"
            return redirect(url_for('pageAnggotaPerpustakaan'))
    # return render_template("register.html")
    return f"berhasil {id}, {nama}, {passwordHash}"


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('admin', None)
    session.pop('id', None)
    session.pop('user', None)
    return redirect(url_for('login'))


def adminLoginRequired(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print('loggedin' not in session)
        print('admin' not in session)
        print('loggedin' not in session and 'admin' not in session)
        if 'loggedin' in session and 'admin' in session:
            # return "anda harus login terlebih dahulu"
            return f(*args, **kwargs)
        return redirect(url_for('login'))
    return decorated_function


def usersLoginRequired(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print('loggedin' not in session)
        print('user' not in session)
        print('loggedin' not in session and 'user' not in session)
        if 'loggedin' in session and 'user' in session:
            return f(*args, **kwargs)
        return redirect(url_for('login'))
    return decorated_function
