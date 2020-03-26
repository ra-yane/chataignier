from flask import Blueprint
from flask_restful import Api, Resource, request

from .plant_data import PlantData

api_bp = Blueprint('api', __name__)


def register_api(app):
    api = Api(api_bp)
    api.add_resource(PlantData, '/plantdata')
    app.register_blueprint(api_bp, url_prefix="/api")