from flask import jsonify, Blueprint, request
from __init__ import db
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
      
@all_routes.route("/create_users", methods=["GET", "POST"])
def create_users():
  data = request.json

  # Extracting data from request
  senior_username = data.get('senior_username')
  senior_password = data.get('senior_password')
  guardian_username = data.get('guardian_username')
  guardian_password = data.get('guardian_password')

  # Check if all necessary data is provided
  if not all([senior_username, senior_password, guardian_username, guardian_password]):
      return jsonify({'error': 'Missing data'}), 400

  try:
    # Check if the senior already exists
    senior_exists = Senior.query.filter_by(username=senior_username).first()
    guardian_exists = Guardian.query.filter_by(guardian_username=guardian_username).first()
    
    if senior_exists or guardian_exists:
        return jsonify({'error': 'Senior or Guardian already exists'}), 400
    
    # Create new Senior and Guardian records
    new_senior = Senior(username=senior_username, password=senior_password)
    new_guardian = Guardian(guardian_username=guardian_username, guardian_password=guardian_password, username=senior_username)
    
    # Add to the session and commit
    db.session.add(new_senior)
    db.session.commit()
    db.session.add(new_guardian)
    db.session.commit()
        
    return jsonify({'message': 'Senior and Guardian created successfully'}), 201

  except Exception as e:
    return jsonify({
        'message': 'Failed to create user!',
        'error' : str(e)
    })