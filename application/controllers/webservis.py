from application import app
from flask import jsonify, request, render_template
from application.models.master.bukuModels import *
from application.models.master.penerbitModels import *
from application.models.master.penulisModels import *
from application.models.master.kategoriModels import *
from application.controllers.auth import adminLoginRequired


@app.route('/mastersBuku', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def mastersBuku():
    
    
    data = {
        "penerbit": getAllpenerbit(),
        "pengarang": getAllpengarang(),
        "kategori": getAllKategori()
    }    

    return jsonify(data)
