from application import app
from flask import jsonify, request, render_template, url_for, redirect, flash
from application.models.master.bukuModels import *
from application.controllers.auth import adminLoginRequired
from application.controllers.webservis import *


@app.route('/master/judulqbuku/<int:id>/buku', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def PageBuku(id):
    
    data = getAllBukuByIdJudulBuku(id)
    judulBuku = getJudulBuku(id)
    print (data)
    return render_template("master/buku.html", all=all, data=data, judulBuku=judulBuku)

