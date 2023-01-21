from application import app
from flask import jsonify, render_template
from application.models.indexModels import *
from application.controllers.auth import adminLoginRequired



@app.route('/', methods=['GET', 'POST'])
@adminLoginRequired
def home():

    data = getjumlahanggota()
    jumlahbuku = getjumlahbuku()
    print (data)

    return render_template("index.html", data=data, jumlahbuku=jumlahbuku)

    # return jsonify(data)

