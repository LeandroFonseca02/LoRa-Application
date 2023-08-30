from flask import Blueprint, jsonify

from models.device import Device
from models.status import Status

status = Blueprint('status', __name__, template_folder='templates')

@status.route('/status')
def status_template():
    all_status = Status.get_all_status()
    return jsonify(all_status)

@status.route('/get_status/<devEUI>', methods=["GET"])
def get_device_status(devEUI):
    device = Device.get_device_by_deveui(devEUI);
    if device is None:
        return jsonify(status=None)
    else:
        status = Status.get_device_status(device.get_device_id())
        return jsonify(status=status.status)