from __init__ import db

class Senior(db.Model):
    __tablename__ = 'Senior'
    username = db.Column(db.String(150), primary_key=True)
    password = db.Column(db.String(150))