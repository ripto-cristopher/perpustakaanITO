from application import app
from flask import jsonify, request, render_template, json
from application.controllers.auth import adminLoginRequired, session
from application.models.master.anggotaPerpustakaanModels import *


@app.route('/master/anggotaPerpustakaan')
@adminLoginRequired
def pageAnggotaPerpustakaan():
    data = getAnggotaPerpustakaans()
    return render_template("master/anggotaPerpustakaan.html", data=data)
