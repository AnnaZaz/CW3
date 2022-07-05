from flask import Flask
from main.view import main_blueprint
from errors.view import blueprint_error
from api.view import api_blueprint

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(blueprint_error)
app.register_blueprint(api_blueprint, url_prefix="/api/")

if __name__ == "__main__":
    app.run(debug=True)
