import json
import flask
from controllers.db import db
from models.application import Application
from models.device import Device
from models.packet import Packet
from models.status import Status



app = flask.Flask(__name__)
with open('config.json') as file:
    data = json.load(file)

app.config['SQLALCHEMY_DATABASE_URI'] = data['database']['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = data['database']['SQLALCHEMY_TRACK_MODIFICATIONS']
db.init_app(app)

if __name__ == "__main__":
    app.app_context().push()
    db.create_all()