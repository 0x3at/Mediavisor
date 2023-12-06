from sqlalchemy.orm import validates
from ..ext.database import DB as db

from .relational import media_server_association_table


class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(80), nullable=False)
    file_size = db.Column(db.Integer, nullable=False)
    popularity = db.Column(db.Integer, nullable=False)
    server_list = db.relationship(
        "Server", secondary=media_server_association_table, back_populates="media_ids"
    )

    def __repr__(self):
        return f"Media(id={self.id}, title={self.title}, description={self.description}, type={self.type}, file_size={self.file_size}, server_list={self.server_list})"

    @validates("popularity")
    def validate_popularity(self, key, value):
        if value < 0 or value > 10:
            raise ValueError(
                "<Failed to add media to DB : popularity must be between 0 and 10>"
            )
        return value

    def to_dict(self):
        return {
            "visibility": "Full",
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "type": self.type,
            "file_size": self.file_size,
            "popularity": self.popularity,
            "server_list": [server.id for server in self.server_list],
        }

    def to_public_dict(self):
        return {
            "visibility": "public",
            "title": self.title,
            "description": self.description,
            "type": self.type,
            "popularity": self.popularity,
        }
