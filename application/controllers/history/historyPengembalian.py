from application import app
from flask import jsonify, request, render_template, url_for, redirect, flash
from application.models.history.historypengembalianModals import *
from application.controllers.auth import adminLoginRequired
from application.controllers.webservis import *


@app.route('/historyPengembalian', methods=['GET', 'POST', 'PUT'])
@adminLoginRequired
def PageHistoryPengembalian():
    data = getHistoryPengembalian()
    print (data)
    return render_template("history/historyPengembalian.html", data= data)
