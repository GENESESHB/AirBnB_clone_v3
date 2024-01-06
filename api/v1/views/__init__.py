#!/usr/bin/python3
""" Blueprint for the Flask web application API."""
from .index import *
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
