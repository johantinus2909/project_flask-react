from exts import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Text

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f"<Recipe {self.title}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def update(self, title, description):
        self.title = title
        self.description = description
        db.session.commit()
        
        
#user model
"""
class User:
    id:integer
    username:string
    email:string
    password:string
"""

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(25), nullable=False, unique=True )
    email=db.Column(db.String(80), nullable=False )
    password=db.Column(db.Text(), nullable=False)
    
    def __repr__(self):
        return f"<User {self.username}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
