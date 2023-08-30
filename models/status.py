from dataclasses import dataclass
from controllers.db import db
import datetime


@dataclass
class Status(db.Model):
    device_id: int
    status: bool
    created_at: str
    updated_at: str

    device_id = db.Column('device_id', db.ForeignKey('device.id'), primary_key=True)
    device = db.relationship('Device', backref='status')
    status = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)

    @staticmethod
    def get_all_status():
        return db.session.query(Status).all()

    @staticmethod
    def update_status(device_id):
        status = db.session.query(Status).filter(Status.device_id == int(device_id)).first()
        status.status = not status.status
        db.session.commit()


    @staticmethod
    def get_device_status(device_id):
        return db.session.query(Status).filter(Status.device_id == int(device_id)).first()
