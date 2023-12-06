from ..ext.database import DB as db
from .relational import media_server_association_table


class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endpoint = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    remaining_storage = db.Column(db.Integer, nullable=False)
    latency = db.Column(db.Float, default=None)
    media_ids = db.relationship(
        "Media", secondary=media_server_association_table, back_populates="server_list"
    )

    def __repr__(self):
        return f"Server(id={self.id}, endpoint={self.endpoint}, is_active={self.is_active}, remaining_storage={self.remaining_storage}, latency = {self.latency},media_ids={self.media_ids})"

    def to_dict(self):
        return {
            "id": self.id,
            "endpoint": self.endpoint,
            "is_active": self.is_active,
            "remaining_storage": self.remaining_storage,
            "latency": self.latency,
            "media_ids": [media.to_dict()['id'] for media in self.media_ids],
        }
