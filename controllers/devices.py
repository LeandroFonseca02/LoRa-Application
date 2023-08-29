from flask import Blueprint, jsonify

from models.device import Device

devices = Blueprint('devices', __name__, template_folder='templates')

@devices.route('/devices')
def devices_template():
    all_devices = Device.get_all_devicess()
    return jsonify(all_devices)

