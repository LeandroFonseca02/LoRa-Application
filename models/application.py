from dataclasses import dataclass
from controllers.db import db

@dataclass
class Application(db.Model):
    id: int
    name: str
    description: str

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

    def __init__(self, name, description):
        self.name = name
        self.description = description


    @staticmethod
    def create_application(name, description):
        app = Application(name=name, description=description)
        db.session.add(app)
        db.session.commit()

    @staticmethod
    def get_appid_by_name(app_name):
        app = db.session.query(Application).filter(Application.name == app_name).first()
        return app.id

    @staticmethod
    def get_all_applications():
        return db.session.query(Application).all()