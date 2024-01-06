#!/usr/bin/python3
"""
create route /status ;
object within the api.v1.views
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def get_status():
    return jsonify({"status": "OK"})

