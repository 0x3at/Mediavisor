from sqlalchemy.orm import joinedload


from ..models import Server
from ..ext.database import DB as db


class ServerInterface:

    @staticmethod
    def retrieve_server_instance(id):
        result = Server.query.filter_by(id=id).options(
            joinedload(Server.media_ids)).first()
        return result

    @staticmethod
    def get_full_list():
        result = [server.to_dict() for server in Server.query.all()]
        if result:
            return result
        return ValueError("No Server in database")

    @staticmethod
    def get_server_by_id(id):
        result = Server.query.filter_by(id=id).first()
        if result:
            return result.to_dict()
        return ValueError(f"Server with id={id} does not exist")

    @staticmethod
    def get_server_by_endpoint(endpoint):
        result = Server.query.filter_by(endpoint=endpoint).first()
        if result:
            return result.to_dict()
        return ValueError(f"Server with endpoint={endpoint} does not exist")

    @staticmethod
    def create_new_server(server_attributes, returns=False):
        new_instance = Server(endpoint=server_attributes['endpoint'],
                              is_active=server_attributes['is_active'],
                              remaining_storage=server_attributes['remaining_storage'])
        db.session.add(new_instance)
        db.session.commit()
        if returns:
            return new_instance.to_dict()

    @staticmethod
    def switch_server_status(id, returns=False):
        result = Server.query.filter_by(id=id).first()
        if result:
            result.is_active = not result.is_active
            db.session.commit()
            if returns:
                return result.to_dict()
        return ValueError(f"Server with id={id} does not exist")

    @staticmethod
    def delete_server_by_id(id):
        result = Server.query.filter_by(id=id).first()
        if result:
            db.session.delete(result)
            db.session.commit()
            return True
        return ValueError(f"Server with id={id} does not exist")

    @staticmethod
    def delete_server_by_endpoint(endpoint):
        result = Server.query.filter_by(endpoint=endpoint).first()
        if result:
            db.session.delete(result)
            db.session.commit()
            return True
        return ValueError(f"Server with endpoint={endpoint} does not exist")

    @staticmethod
    def update_server_by_id(id, values: dict, returns=False):
        result = Server.query.filter_by(id=id).first()
        if result:
            for key, value in values.items():
                setattr(result, key, value)
        db.session.commit()
        if returns:
            return result.to_dict()

    @staticmethod
    def add_media_to_relational_mapping(media, server, returns=False):
        server_instance = ServerInterface.retrieve_server_instance(
            server['id'])
        server_instance.media_ids.append(media)
        db.session.commit()
        if returns:
            instance_dict = server_instance.to_dict()
            return {instance_dict['id']: instance_dict['media_ids']}

    @staticmethod
    def get_media_ids_on_server(server_id):
        server = ServerInterface.retrieve_server_instance(server_id)
        return [media.id for media in server.media_ids]
