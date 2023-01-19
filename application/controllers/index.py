from application import app
from flask import jsonify, render_template
from application.models.indexModels import *
from application.controllers.auth import adminLoginRequired



@app.route('/', methods=['GET', 'POST'])
@adminLoginRequired
def home():

    data = getDate()

    return render_template("index.html")

    # return jsonify(data)
