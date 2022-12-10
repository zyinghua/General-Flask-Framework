from flask import Blueprint

api1 = Blueprint('api1', __name__)


@api1.route('/', methods=['GET', 'POST', 'DELETE', 'UPDATE'])  # define HTTP methods for this function/end point
def index():
    """define REST-ful logic here..."""
    return "API ENTRY 1"

