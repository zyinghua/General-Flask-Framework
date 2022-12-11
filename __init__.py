from flask import Flask, render_template
from routes.api import api  # import the Blueprint named as 'api'
from database import db_session, init_db, drop_db


def create_app():
    app = Flask(__name__)

    """----------------------------------------------"""
    """Disable the SQLAlchemy event notification system."""
    """Further Info: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/"""
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    """-----------------------------------------------"""

    """----------------------------------------------"""
    """!PLEASE GENERATE YOUR OWN SECRET_KEY!"""
    """One way to generate secret key byte string: """
    """import secrets; secrets.token_bytes([nbytes=None])"""
    """The secret key is needed to keep the client-side sessions secure."""
    """Secret key is a random key used to encrypt your cookies and safely send them to the browser."""
    app.config['SECRET_KEY'] = b'r\xb3\xda\r\xff\x82\xa6\x0fb\x9cdN\xe3\xa8{wP\x1en\xe9y\xd0\xaap\xdc\xe6z.\xc7\xea'
    """-----------------------------------------------"""

    app.register_blueprint(api, url_prefix='/api')

    """---------------------------------"""
    """An example of registering a route"""
    """  Access this route: {BASE URL}  """
    @app.route('/')
    def index():
        """
        render_template can render an HTML page in the
        browser when this route is reached.
        """
        return render_template('index.html')
    """---------------------------------"""

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    init_db()  # initialise the database
    # drop_db()  # uncomment to drop the database

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
