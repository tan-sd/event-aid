from __init__ import db

class Planner(db.Model):
    __tablename__ = 'Planner'
    username = db.Column(db.String(150), primary_key=True)
    passowrd = db.Column(db.String(150))