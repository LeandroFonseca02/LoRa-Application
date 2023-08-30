import json

from flask import Flask, render_template

from controllers.applications import applications
from controllers.db import db
from controllers.devices import devices
from controllers.packets import packets
from controllers.status import status

app = Flask(__name__)
with open('./config/config.json') as file:
    data = json.load(file)


app.config['SQLALCHEMY_DATABASE_URI'] = data['database']['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = data['database']['SQLALCHEMY_TRACK_MODIFICATIONS']
app.config['SECRET_KEY'] = data['SECRET_KEY']


# login_manager.init_app(app)

with app.app_context():
    db.init_app(app)


@app.route('/')
# @login_required
def index_template():
    #return "LoRa APP Running"

    return render_template('index.html')



app.register_blueprint(devices)
app.register_blueprint(applications)
app.register_blueprint(packets)
app.register_blueprint(status)
# app.register_blueprint(vehicles)
# app.register_blueprint(rides)
# app.register_blueprint(reservations)
# app.register_blueprint(roles)
# app.register_blueprint(ratings)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
