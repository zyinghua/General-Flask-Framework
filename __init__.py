from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = b'\xed\xeeM\xaaK\r\xc0@xw@\xb6\xd0 S9[z\xde$\xc6\x9a\x13}\xa3\xfa\xdb[\xb1\x98\x08\xa9'

    app.register_blueprint()


    return app


if __name__ == '__main__':
    create_app().run(debug=False)