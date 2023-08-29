from flask import Blueprint, jsonify

from models.application import Application

applications = Blueprint('applications', __name__, template_folder='templates')

@applications.route('/applications')
def applications_template():
    all_applications = Application.get_all_applications()
    return jsonify(all_applications)

