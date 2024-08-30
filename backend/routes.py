from flask import jsonify, Blueprint , request
from models.event import Event
from models.guardian import Guardian
from models.planner import Planner
from models.senior import Senior
from models.user_event import User_event
from datetime import datetime
from __init__ import db

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

@all_routes.route("/create_event" , methods=["POST"])
def create_event():
    try:
        data = request.get_json()
        required_fields = ['location' , 'title' , 'description' , 'planner_username']

        for field in required_fields:
          if field not in data:
              return jsonify({'code': 400, 'message': f"'{field}' is missing in the request data"}), 400
          
        planner = db.session.query(Planner).filter_by(username=data['planner_username']).first()
        if not planner:
            return jsonify({'code': 404, 'message': 'Planner username not found'}), 404
          
        new_event = Event(
            location=data['location'],
            title=data['title'],
            description=data['description'],
            planner_username=data['planner_username'],
            datetime=datetime.now()  
        )

        db.session.add(new_event)
        db.session.commit()

        return jsonify(
            {
                "code": 200,
                'message': "Successfully created event to the database",
            }
        ), 200


    except Exception as e:
      return jsonify(
          {
              "code": 500,
              "message": f"An error occurred while retrieving the applicants, {str(e)}"
          }
    ), 500