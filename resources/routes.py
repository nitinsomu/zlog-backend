from flask import Blueprint
from flask_restful import Api
#
from resources.register import Register
from resources.login import Login

base_route = '/'
zlog_blueprint = Blueprint('zlog_blueprint', __name__, url_prefix=base_route)
zlog_api = Api(zlog_blueprint)

zlog_api.add_resource(
    Register,
    '/register'
)

zlog_api.add_resource(
    Login,
    '/login'
)