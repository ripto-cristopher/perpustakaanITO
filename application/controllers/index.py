from application import app
from flask import jsonify
from application.models.indexModels import *
from application.controllers.auth import adminLoginRequired



@app.route('/', methods=['GET', 'POST'])
@adminLoginRequired
def index():

    data = getDate()


    return jsonify(data)