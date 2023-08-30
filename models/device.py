import datetime
from dataclasses import dataclass

from sqlalchemy import text

from controllers.db import db
from models.application import Application
from models.status import Status


@dataclass
class Device(db.Model):
    id: int
    deveui: str
    board: str
    app_id: int
    created_at: str
    updated_at: str

    id = db.Column(db.Integer, primary_key=True)
    deveui = db.Column(db.String(255), unique=True)
    board = db.Column(db.String(255))
    app_id = db.Column('app_id', db.ForeignKey('application.id'))
    app = db.relationship('Application', backref='application')
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def get_device_id(self):
        return self.id

    @staticmethod
    def get_all_devices():
        return db.session.query(Device).all()

    @staticmethod
    def get_all_devices_status():
        query = text("""SELECT id, deveui, board, app_id, s.status, d.created_at as created_at, d.updated_at as updated_at
                        FROM device d, status s
                        WHERE d.id = s.device_id""")

        return db.session.execute(query).all()

    @staticmethod
    def get_all_devices_by_app_id(app_id):
        return db.session.query(Device).filter(Device.app_id == app_id).all()

    @staticmethod
    def get_device_by_deveui(deveui):
        return db.session.query(Device).filter(Device.deveui == deveui).first()

    @staticmethod
    def get_device_by_id(id):
        return db.session.query(Device).filter(Device.id == id).first()


    def get_device_app_id(self):
        return self.app_id

    @staticmethod
    def update_board(deveui, board):
        device = Device.get_device_by_deveui(deveui)
        device.board = board
        device.updated_at = datetime.datetime.now()
        db.session.commit()

    @staticmethod
    def create_device(deveui, board, app_name):
        device = Device(deveui=deveui, board=board, app_id=Application.get_appid_by_name(app_name))
        db.session.add(device)
        db.session.commit()

        if device.get_device_app_id() == Application.get_appid_by_name("GPS Tracker"):
            Device.create_device_status(device.get_device_id())



    @staticmethod
    def delete_device(id):
        db.session.query(Device).filter(Device.id == int(id)).delete()
        db.session.commit()

    def __str__(self):
        return self.deveui


    # @staticmethod
    # def add_role(user_id, role_id):
    #     query = "INSERT INTO role_user VALUES (" + user_id + ", " + role_id + ")"
    #     db.session.execute(query)
    #     db.session.commit()

    @staticmethod
    def get_number_nodes():
        return len(db.session.query(Device).all())


    @staticmethod
    def create_device_status(device_id):
        status = Status(device_id=device_id)
        db.session.add(status)
        db.session.commit()