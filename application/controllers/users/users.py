from application import app
from flask import jsonify, render_template
from application.controllers.auth import adminLoginRequired
from application.models.master.bukuModels import *


@app.route('/u', methods=['GET', 'POST'])
def usersHome():

    data = getAllJudulBuku()


    return render_template("users/usersHome.html", data=data)

    # return jsonify(data)
