from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

matches = db.Table("matches",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("course.id"), primary_key=True)
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, index=True)
    email = db.Column(db.String(40), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    matches = db.relationship("Course", secondary=matches, lazy="subquery", backref=db.backref("users", lazy=True))

    def __repr__(self):
        return "<Type object %s>" % self.username

    #password isn't a readable attribute
    @property
    def password(self):
        raise AttributeError('Forbbiden')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    start1 = db.Column(db.Integer)
    end1 = db.Column(db.Integer)
    day1 = db.Column(db.Integer, default=0)
    split_time = db.Column(db.Boolean, default=False)
    start2 = db.Column(db.Integer, default=0)
    end2 = db.Column(db.Integer, default=0)
    day2 = db.Column(db.Integer, default=0)
    type1 = db.Column(db.String(40))
    type2 = db.Column(db.String(40))
    section = db.Column(db.String(3))

    def __repr__(self):
        return "<Type object %s (%s)>" % (self.name, self.section)

from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)