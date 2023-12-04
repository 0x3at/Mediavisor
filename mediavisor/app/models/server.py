from app.models import db
from app.models.relational import media_server_association_table


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
            "media_ids": self.media_ids,
        }

    def switch_server_status(self):
        self.is_active = not self.is_active
        db.session.commit()

    @staticmethod
    def __build_new_self(endpoint, is_active, remaining_storage):
        return Server(
            endpoint=endpoint, is_active=is_active, remaining_storage=remaining_storage
        )

    @staticmethod
    def get_full_server_list():
        return [server.to_dict() for server in Server.query.all()]

    @staticmethod
    def get_server_by_id(id):
        server_result = Server.query.filter_by(id=id).first()
        return server_result.to_dict()

    @staticmethod
    def get_server_by_endpoint(endpoint):
        server_result = Server.query.filter_by(endpoint=endpoint).first()
        return server_result.to_dict()

    @staticmethod
    def create_new_server(endpoint, is_active, remaining_storage, returns=False):
        new_server = Server.__build_new_self(endpoint, is_active, remaining_storage)
        db.session.add(new_server)
        db.session.commit()
        if returns:
            return new_server.to_dict()

    @staticmethod
    def retrieve_server_instance(id):
        return Server.query.filter_by(id=id).first()

    @staticmethod
    def delete_server_by_id(id):
        server_to_delete = Server.query.filter_by(id=id).first()
        db.session.delete(server_to_delete)
        db.session.commit()

    @staticmethod
    def delete_server_by_endpoint(endpoint):
        server_to_delete = Server.query.filter_by(endpoint=endpoint).first()
        db.session.delete(server_to_delete)
        db.session.commit()

    @staticmethod
    def update_server_by_id(id, values: list[dict]):
        server_to_update = Server.query.filter_by(id=id).first()
        for dict in values:
            for key, value in dict.items():
                setattr(server_to_update, key, value)
        db.session.commit()
