from __init__ import db

class Senior(db.Model):
    __tablename__ = 'Senior'
    username = db.Column(db.String(150), primary_key=True)
    passowrd = db.Column(db.String(150))