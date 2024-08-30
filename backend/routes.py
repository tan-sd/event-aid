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
        }), 200
      
      except Exception as e:
        return jsonify({
            'message': 'Failed to retrieve events!',
            'error' : str(e)
        }), 400

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
      
@all_routes.route('/delete_event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    query_delete_listing = Event.query.filter_by(event_id=event_id).all()[0]

    try:
        db.session.delete(query_delete_listing)
        db.session.commit()

        return jsonify({
            'isDeleted': True,
            'message': f'Event id {event_id} has been deleted!'
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({
            'isApplied': False,
            'message': f'Failed to delete event id {event_id}!',
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
    }), 400
  
@all_routes.route("/create_user_event", methods=["POST"])
def create_user_event():
    data = request.json
    senior_username = data.get('senior_username')
    event_id = data.get('event_id')
    is_sign_up = data.get('is_sign_up')
    is_confirmed = data.get('is_confirmed')

    try:
      user_event = User_event(senior_username=senior_username, event_id=event_id, is_sign_up=is_sign_up, is_confirmed=is_confirmed)
      db.session.add(user_event)
      db.session.commit()
      return jsonify({'message': 'You have expressed interest in this event.'}), 201
    
    except Exception as e:
      return jsonify({
          'message': 'Expression of interest for this event has failed.',
          'error' : str(e)
      }), 400

@all_routes.route("/get_user_event_by_user/<senior_username>", methods=["GET"])
def get_user_event_by_user(senior_username):
    try:
        query_results = User_event.query.filter_by(senior_username=senior_username).all()
        user_events = []

        if len(query_results) == 0:
           return jsonify({
                'message': "There are no events of interest.",
                "data": user_events
            }), 200
        
        for event in query_results:
            event_dict = {}
            event_dict['event_id'] = event.event_id
            event_dict['senior_username'] = event.senior_username
            event_dict['is_sign_up'] = event.is_sign_up
            event_dict['is_confirmed'] = event.is_confirmed
            user_events.append(event_dict)
            
            return jsonify({
                'message': "Successfully retrieved all events of interest.",
                "data": user_events
            }), 200
      
    except Exception as e:
        return jsonify({
            'message': 'Failed to retrieve events!',
            'error' : str(e)
        }), 400
    
  
@all_routes.route("/update_event/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    try:
        event = db.session.query(User_event).filter_by(event_id=event_id).first()

        if not event:
            return jsonify({'code': 404, 'message': 'Event not found'}), 404

        data = request.get_json()

        if 'is_sign_up' in data:
            event.is_sign_up = True

        db.session.commit()
        return jsonify({'code': 200, 'message': 'Event updated successfully'}), 200
    except Exception as e:
        return jsonify({'code': 500, 'message': str(e)}), 500