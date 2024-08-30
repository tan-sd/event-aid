from sqlalchemy import ForeignKey
from __init__ import db

class Guardian(db.Model):
    __tablename__ = 'Guardian'
    guardian_username = db.Column(db.String(150), primary_key=True)
    guardian_password = db.Column(db.String(150))
    username = db.Column(db.String(150), ForeignKey('Senior.username'), primary_key=True)