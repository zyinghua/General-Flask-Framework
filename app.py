from flask import Flask, render_template
from routes.api import api  # import the Blueprint named as api1


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = b'\xed\xeeM\xaaK\r\xc0@xw@\xb6\xd0 S9[z\xde$\xc6\x9a\x13}\xa3\xfa\xdb[\xb1\x98\x08\xa9'

    app.register_blueprint(api, url_prefix='/api')

    """---------------------------------"""
    """An example of registering a route"""
    @app.route('/')
    def index():
        """
        render_template can render an HTML page in the
        browser when this route is reached.
        """
        return render_template('index.html')
    """---------------------------------"""

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
