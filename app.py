from flask import Flask
import pickle

from views import app as fake_news

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.DevelopmentConfig')

#   Setup dependencies

#   Register Blue prints
    app.register_blueprint(fake_news)

    return app

if __name__ == "__main__":
    create_app().run()
 