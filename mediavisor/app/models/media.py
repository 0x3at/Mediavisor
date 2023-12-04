from sqlalchemy.orm import validates

from app.models import db
from app.models.relational import media_server_association_table


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

    @validates("popularity")
    def validate_popularity(self, key, value):
        if value < 0 or value > 10:
            raise ValueError(
                "<Failed to add media to DB : popularity must be between 0 and 10>"
            )
        return value

    def __repr__(self):
        return f"Media(id={self.id}, title={self.title}, description={self.description}, type={self.type}, file_size={self.file_size}, server_list={self.server_list})"

    def to_dict(self):
        return {
            "visibility": "Full",
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "type": self.type,
            "file_size": self.file_size,
            "popularity": self.popularity,
            "server_list": self.server_list,
        }

    def to_public_dict(self):
        return {
            "visibility": "public",
            "title": self.title,
            "description": self.description,
            "type": self.type,
            "popularity": self.popularity,
        }

    @staticmethod
    def __build_new_self(title, description, type, file_size, popularity):
        return Media(
            title=title,
            description=description,
            type=type,
            file_size=file_size,
            popularity=popularity,
        )

    @staticmethod
    def get_full_media_list():
        return [media.to_dict() for media in Media.query.all()]

    @staticmethod
    def get_media_by_title(title, visibility="public"):
        if visibility == "public":
            media_result = [
                media.to_public_dict()
                for media in Media.query.filter_by(title=title).all()
            ]
            if len(media_result) == 0:
                return None
            if len(media_result) > 1:
                return media_result

            return media_result[0]

    @staticmethod
    def get_media_by_id(id):
        media_result = Media.query.filter_by(id=id).first()
        if media_result is None:
            return None
        return media_result.to_dict()

    @staticmethod
    def retrieve_media_instance(id):
        return Media.query.filter_by(id=id).first()

    @staticmethod
    def create_new_media(
        title, description, type, file_size, popularity, returns=False
    ):
        new_media = Media.__build_new_self(
            title, description, type, file_size, popularity
        )
        db.session.add(new_media)
        db.session.commit()
        if returns:
            return new_media.to_dict()

    @staticmethod
    def delete_media_by_id(id):
        media_to_delete = Media.query.filter_by(id=id).first()
        db.session.delete(media_to_delete)
        db.session.commit()
