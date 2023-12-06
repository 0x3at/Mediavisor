from ..ext.database import DB as db


class TestBool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bool = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"TestBool(id={self.id}, bool={self.bool})"

    def to_dict(self):
        return {
            "id": self.id,
            "bool": self.bool,
        }
