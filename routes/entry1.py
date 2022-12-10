from flask import Blueprint

entry1 = Blueprint('entry1', __name__)


@entry1.route('/', methods=['GET', 'POST', 'DELETE', 'UPDATE'])  # define HTTP methods for this function/end point
def index():
    """
    define your REST-ful logic here...
    e.g.: Data processing, Database manipulations...
    """
    return "API ENTRY POINT 1"

