from . import db

matches = db.Table("matches",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("course.id"), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    matches = db.relationship("Course", secondary=matches, lazy="subquery", backref=db.backref("users", lazy=True))

    def __repr__(self):
        return "<Type object %s>" % self.name

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
        return "<Type object %s>" % self.name
