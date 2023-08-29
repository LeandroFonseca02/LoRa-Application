from flask import Blueprint, jsonify

from models.status import Status

status = Blueprint('status', __name__, template_folder='templates')

@status.route('/status')
def status_template():
    all_status = Status.get_all_status()
    return jsonify(all_status)

