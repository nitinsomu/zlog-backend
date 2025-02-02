from flask import Blueprint
from flask_restful import Api
#
from resources.post import Post
from resources.login import Login
from resources.logout import Logout
from resources.profile import Profile
from resources.register import Register

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

zlog_api.add_resource(
    Profile,
    '/profile'
)

zlog_api.add_resource(
    Logout,
    '/logout'
)

zlog_api.add_resource(
    Post,
    '/post'
)

