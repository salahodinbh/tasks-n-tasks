"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Task API"
    }
)


def create_app(app_name='TASK_API'):
    app = Flask(app_name)
    app.config.from_object('taskapi.config.BaseConfig')

    from taskapi.api import api
    app.register_blueprint(api, url_prefix="/api")

    from taskapi.models import db
    db.init_app(app)

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    # Esto si falta empieza a dar por saco el flask db init
    migrate = Migrate(app, db)
    
    return app