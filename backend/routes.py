from flask import jsonify, Blueprint
from models.event import Event
from models.guardian import Guardian
from models.planner import Planner
from models.senior import Senior
from models.user_event import User_event

all_routes = Blueprint('all', __name__)

@all_routes.route("/all_event_details", methods=["GET"])
def get_all_event():
      try:
        event_query_list = Event.query.all()
        event_list = []
        for event in event_query_list:
            event_dict = {}
            event_dict['id'] = event.event_id
            event_dict['datetime'] = event.datetime
            event_dict['location'] = event.location
            event_dict['title'] = event.title
            event_dict['description'] = event.description
            event_dict['planner_username'] = event.planner_username

            event_list.append(event_dict)
        
        return jsonify({
            'message': "Successfully retrieved data from database",
            "data": event_list
        })
      
      except Exception as e:
        return jsonify({
            'message': 'Failed to retrieve events!',
            'error' : str(e)
        })