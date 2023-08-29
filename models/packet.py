from dataclasses import dataclass
import datetime

from controllers.db import db
from models.device import Device


@dataclass
class Packet(db.Model):
    id: int
    device_id: int
    type: str
    data: str
    rssi: int
    created_at: str

    id = db.Column(db.Integer(), primary_key=True)
    device_id = db.Column('device_id', db.ForeignKey('device.id'))
    device = db.relationship('Device', backref='device')
    type = db.Column(db.String(255))
    data = db.Column(db.String(255))
    rssi = db.Column(db.Integer())
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)



    @staticmethod
    def get_all_packets_by_device_id(device_id):
        return db.session.query(Device).filter(Device.id == device_id).all()

    @staticmethod
    def get_all_packets():
        return db.session.query(Device).all()

    @staticmethod
    def create_packet(device_id, data):
        packet = Packet(device_id=device_id, data=data)
        db.session.add(packet)
        db.session.commit()
        return packet