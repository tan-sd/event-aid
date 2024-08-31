from sqlalchemy import ForeignKey
from __init__ import db

class Event(db.Model):
    __tablename__ = 'Event'
    event_id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime(timezone=True))
    location = db.Column(db.String(300))
    title = db.Column(db.String(300))
    description = db.Column(db.String(300))
    planner_username = db.Column(db.String(100), ForeignKey('Planner.username'))