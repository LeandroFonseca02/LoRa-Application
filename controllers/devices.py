from flask import Blueprint, jsonify, render_template

from models.application import Application
from models.device import Device

devices = Blueprint('devices', __name__, template_folder='templates')

@devices.route('/devices/AGPS')
def devices_agps():
    all_devices = Device.get_all_devices_status()
    return render_template('devices.html', devices=all_devices, app="agps")

@devices.route('/devices/WT')
def devices_wt():
    all_devices = Device.get_all_devices_by_app_id(Application.get_appid_by_name("Water Tank"))
    return render_template('devices.html', devices=all_devices, app="wt")
