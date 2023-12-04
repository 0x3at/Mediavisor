from flask import Blueprint
from flask_restful import Api


from app.api.public_blueprints import IsActiveEndpoint

public_ping_blueprint = Blueprint("public_ping", __name__)
public_ping_api = Api(public_ping_blueprint)

public_ping_api.add_resource(IsActiveEndpoint, "/ping")
