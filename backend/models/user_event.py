from sqlalchemy import ForeignKey
from __init__ import db

class User_event(db.Model):
    __tablename__ = 'User_event'
    event_id = db.Column(db.Integer, ForeignKey('Event.event_id'), primary_key=True)
    senior_username = db.Column(db.String(100), ForeignKey('Senior.username'), primary_key=True)
    is_sign_up = db.Column(db.Boolean)
    is_confirmed = db.Column(db.Boolean)