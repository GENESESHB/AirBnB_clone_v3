#!/usr/bin/python3
"""
the file states
"""

from api.v1.views import app_views
from flask import Flask, abort, jsonify, make_response, request
from werkzeug.exceptions import HTTPException
from models import storage
from models.state import State



@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """
    get state information for all states in storage
    """
    states = []
    for state in storage.all(State).values():
        states.append(state.to_dict())
    return jsonify(states)


@app_views.route("/states/<string:state_id>", methods=['GET'],
        strict_slashes=False)
def get_state(state_id):
    """
    get state information for specified state
    into storage
    """
    state = storage.get(State, state_id)
    if state:
        return jsonify(state.to_dict())
    abort(404)


@app_views.route("/states/<state_id>", methods=['DELETE'])
def delete_state(state_id):
    """
    delet a state into storage based on state_id
    """
    state = storage.get(State, state_id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def post_state():
    """
    create a new state into storage and save him
    """
    if not request.is_json():
        abort(400, 'Not a JSON')

    bdy = request.get_json()
    if not bdy.get("name"):
        abort(400, "Missing name")
    new_state = State(**bdy)
    storage.new(new_state)
    storage.save()
    return jsonify(new_state.to_dict()), 201


@ app_views.route('/states/<string:state_id>', methods=['PUT'],
    strict_slashes=False)
def update_state():
    """
    updated state in storage and save the change
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.is_json():
        abort(400, "Not a JSON")
    bdy = request.get_json()
    ignrd_key = ['id', 'created_at', 'updated_at']
    for key, value in bdy.items():
        if key not in ignrd_key:
            setattr(state, key, value)
    storage.save()
    return jsonify(obj.to_dict())
