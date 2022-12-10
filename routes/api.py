from flask import Blueprint
from routes.entry1 import entry1
from routes.entry2 import entry2

api = Blueprint('api', __name__)

"""A Blueprint can also register another blueprints, like sub-trees."""
api.register_blueprint(entry1, url_prefix="/entry1")
api.register_blueprint(entry2, url_prefix="/entry2")


@api.route('/', methods=['GET', 'POST', 'DELETE', 'UPDATE'])  # define HTTP methods for this function/end point
def index():
    """
    define your REST-ful logic here...
    e.g.: Data processing, Database manipulations...
    """
    return "{BASE URL}/API/..."
