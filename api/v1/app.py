#!/usr/bin/python3
''' Flask application '''
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import environ
from flask_cors import CORS


app = Flask(__name__)

app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    ''' Error 404 '''
    return {"error": "Not found"}, 404


if __name__ == "__main__":
    host = environ.get("HBNB_API_HOST", "0.0.0.0")
    port = int(environ.get("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
