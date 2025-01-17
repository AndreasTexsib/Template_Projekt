''' script for the routes of the web service '''

# pylint: disable=unused-variable

from flask import render_template, request

from src.database.database import get_db
from src.util import config_util


def init_routes(app):
    ''' init the routes for the web service '''

    # Main View
    @app.route('/', methods= ['GET'])
    def index():
        with get_db().cursor() as cursor:
            return render_template("index.html.j2")
