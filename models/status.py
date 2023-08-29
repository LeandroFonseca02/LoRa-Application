from dataclasses import dataclass
from controllers.db import db


@dataclass
class Status(db.Model):
    device_id: int
    status: bool

    device_id = db.Column('device_id', db.ForeignKey('device.id'), primary_key=True)
    device = db.relationship('Device', backref='status')
    status = db.Column(db.Boolean())

    def __str__(self):
        return self.name

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @staticmethod
    def get_all_status():
        return db.session.query(Status).all()
