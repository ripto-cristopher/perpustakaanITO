from application import app
from flask import jsonify, request, render_template, url_for, redirect, flash
from application.models.history.historyPeminjamanModals import *
from application.controllers.auth import adminLoginRequired


@app.route('/historypeminjaman', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def PageHistoryPeminjaman():
    data = getHistoryPengembalian()
    return render_template("history/historyPeminjaman.html", data=data)
