from flask import Blueprint, jsonify, render_template, redirect

from forms import CreateDeviceForm
from models.application import Application
from models.device import Device

devices = Blueprint('devices', __name__, template_folder='templates')

@devices.route('/devices/GPS')
def devices_agps():
    form = CreateDeviceForm()
    app_id = Application.get_appid_by_name("GPS Tracker")
    all_devices = Device.get_all_devices_status()
    return render_template('devices.html', devices=all_devices, app="agps", page="devicesgps", form=form, app_id=app_id)

@devices.route('/devices/WT')
def devices_wt():
    form = CreateDeviceForm()
    app_id = Application.get_appid_by_name("Water Tank")
    all_devices = Device.get_all_devices_by_app_id(Application.get_appid_by_name("Water Tank"))
    return render_template('devices.html', devices=all_devices, app="wt", page="deviceswt", form=form, app_id=app_id)


@devices.route('/createDevice/<app_id>', methods=['POST'])
def create_device(app_id):
    form = CreateDeviceForm()
    if form.is_submitted():
        Device.create_device(deveui=form.deveui.data, board=form.board.data, app_id=app_id)
        if int(app_id) == Application.get_appid_by_name("Water Tank"):
            return redirect('/devices/WT')
        elif int(app_id) == Application.get_appid_by_name("GPS Tracker"):
            return redirect('/devices/GPS')
    return redirect('/')