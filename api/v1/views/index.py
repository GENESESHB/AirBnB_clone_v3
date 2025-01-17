#!/usr/bin/python3
"""
create route /status ;
object within the api.v1.views
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', strict_slashes=False)
def get_status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def get_stats():
    """
    Retrieves the number of each object by type.
    """
    try:
        stats = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
        }
        return jsonify(stats)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
