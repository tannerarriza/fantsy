from app import db


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return "{}".format(self.name)


class Point(db.Model):
    """"""
    __tablename__ = "points"

    id = db.Column(db.Integer, primary_key=True)
    

    points_id = db.Column(db.Integer, db.ForeignKey("points.id"))
    point = db.relationship("Point", backref=db.backref(
        "points", order_by=id), lazy=True)
