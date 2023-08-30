from dataclasses import dataclass
from controllers.db import db


@dataclass
class Status(db.Model):
    device_id: int
    status: bool

    device_id = db.Column('device_id', db.ForeignKey('device.id'), primary_key=True)
    device = db.relationship('Device', backref='status')
    status = db.Column(db.Boolean(), default=False)


    @staticmethod
    def get_all_status():
        return db.session.query(Status).all()

    @staticmethod
    def get_device_status(device_id):
        return db.session.query(Status).filter(Status.device_id == int(device_id)).first()
