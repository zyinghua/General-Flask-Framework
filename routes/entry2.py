from flask import Blueprint

entry2 = Blueprint('entry2', __name__)


@entry2.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])  # define HTTP endpoint & methods for this function
def index():
    """
    define your REST-ful logic here...
    e.g.: Data processing, Database manipulations...
    """
    return "API ENTRY POINT 2"

