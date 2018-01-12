from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#users
class User(UserMixin,db.Model):
    '''
    user class to create new users
    '''
    __tablename__ = 'users'

    #addidng columns
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    comment = db.relationship("Comments", backref="user", lazy = "dynamic")

    #password security
    @property
    def password(self):
        raise AttributeError('you can not read the password Attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


#comments
class Comments(db.Model):
    '''
     class that creates new comments for users
    '''
    __tablename__ = 'comments'

    #columns
    id = db.Column(db.Integer,primary_key = True)
    comment_section_id = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_comment(self):
        '''
        saves the comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self,id):
        comment = Comments.query.order_by(Comments.date_posted.desc()).filter_by(pitches_id = id).all()
        return comment

class Meals:
    """Meals class to define the meals object"""

    def __init__(self, idMeal, strMeal, strCategory, strArea, strInstructions, strMealThumb, strTags,strMeasure1, strIngridients1, strYoutube):
        self.idMeal = idMeal
        self.strMeal = strMeal
        self.strCategory = strCategory
        self.strArea = strArea
        self.strInstructions = strInstructions
        self.strMealThumb = strMealThumb
        self.strTags = strTags
        self.strMeasure1 = strMeasure1
        self.strIngridients1 = strIngridients1
        self.strYoutube = strYoutube



class Category:
    """Category class to define the meals object"""

    def __init__(self,strCategory):
        self.strCategory = strCategory
        

class Search:
    """Search class to define the meals object"""

    def __init__(self, idMeal, strMeal, strCategory, strArea, strInstructions, strMealThumb, strTags,strMeasure1, strIngridients1):
        self.idMeal = idMeal
        self.strMeal = strMeal
        self.strCategory = strCategory
        self.strArea = strArea
        self.strInstructions = strInstructions
        self.strMealThumb = strMealThumb
        self.strTags = strTags
        self.strMeasure1 = strMeasure1
        self.strIngridients1 = strIngridients1
        