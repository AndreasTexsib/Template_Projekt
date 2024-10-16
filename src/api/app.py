''' Initialize the app '''

from flask import Flask

from src.api import routes
from src.database import database

from src.api.blueprints.blueprint import bp

def create_app():
    ''' create the app '''

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        CONFIG_FILE = "src/api/app.ini",
    )

    # init the database
    database.init_db(app)

    # init the routes
    routes.init_routes(app)

    app.register_blueprint(bp)

    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=8000, debug=True)
    # change the port for the current project
    # use ssl_context="adhoc" for testing local https
