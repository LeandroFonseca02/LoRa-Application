from dataclasses import dataclass
import datetime

from sqlalchemy import text

from controllers.db import db
from models.device import Device


@dataclass
class Packet(db.Model):
    id: int
    device_id: int
    type: str
    data: str
    created_at: str

    id = db.Column(db.Integer(), primary_key=True)
    device_id = db.Column('device_id', db.ForeignKey('device.id'))
    device = db.relationship('Device', backref='device')
    type = db.Column(db.String(255))
    data = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)



    @staticmethod
    def get_all_packets_by_device_id(device_id):
        return db.session.query(Packet).filter(Packet.device_id == device_id).all()

    @staticmethod
    def get_all_packets_by_app_id(app_id):
        query = text("""SELECT packet.id as id, device_id, type, data, packet.created_at as created_at
                FROM packet, device as d
                WHERE packet.device_id = d.id
                AND app_id =""" + str(app_id))

        return db.session.execute(query).all()

    @staticmethod
    def get_all_packets():
        return db.session.query(Packet).all()

    @staticmethod
    def create_packet(device_id, type, data):
        packet = Packet(device_id=device_id, type=type, data=data)
        db.session.add(packet)
        db.session.commit()
        return packet
