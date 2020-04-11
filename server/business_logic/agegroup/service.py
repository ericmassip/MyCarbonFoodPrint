from flask import Blueprint, jsonify
from business_logic.agegroup.controller import AgeGroupController

agegroup_service = Blueprint('agegroup_service', __name__)


class AgeGroupService:
    @staticmethod
    @agegroup_service.route('/all')
    def get_all():
        """Get all Age Groups"""

        return jsonify(AgeGroupController.get_all())
