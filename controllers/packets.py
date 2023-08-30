from flask import Blueprint, jsonify, request

from models.application import Application
from models.packet import Packet
from models.device import Device

packets = Blueprint('messages', __name__, template_folder='templates')

@packets.route('/packets')
def packets_template():
    all_packets = Packet.get_all_packets()
    return jsonify(all_packets)

@packets.route('/new_packet', methods=['POST'])
def new_packet():
    json = request.get_json()
    device = Device.get_device_by_deveui(json["devEUI"])
    if device is not None:
        if json["data"].get("status") is not None:
            type = "Status Request"
        else:
            type = str(json["application"])

        data = str(json["data"])
        packet = Packet.create_packet(device_id=device.get_device_id(), type=type, data=data)

        return jsonify(packet)
    else:
        return "Wrong Packet"