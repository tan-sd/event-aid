from __init__ import db

class Planner(db.Model):
    __tablename__ = 'Planner'
    username = db.Column(db.String(150), primary_key=True)
    password = db.Column(db.String(150))