from flask import Blueprint, jsonify, request

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
    data = str(json["data"])
    packet = Packet.create_packet(device_id=device.get_device_by_id(), data=data)

    return jsonify(packet)