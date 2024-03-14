from config import db

class User_Details(db.Model):
    __tablename__="User_Details"

    email=db.Column(db.String(30),primary_key=True)
    name=db.Column(db.String(30))
    password=db.Column(db.String(30))
    designation=db.Column(db.String(30))
    age=db.Column(db.String(4))

    def make_json(self):
        return {c.name:getattr(self,c.name) for c in self.__table__.columns}