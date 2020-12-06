from app import db
# from models.base import BaseModel
from models.user import User
from models.site import Site


class Favourites(db.Model):

  __tablename__ = 'favourites'

  user_id = db.Column(db.Integer, db.ForeignKey('users.id'),  primary_key=True)
  site_id = db.Column(db.Integer, db.ForeignKey('sites.id'),  primary_key=True)
      # unique=True it shouldn't be unique it means is unique in the table so 
      # I cant add it if you have it in your fav

 
  # user = db.relationship('User', backref='favourites')
  # site = db.relationship('Site', backref='favourites') 
  def save(self):
   db.session.add(self)
   db.session.commit()