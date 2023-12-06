from ..models import Media
from ..ext.database import DB as db


class MediaInterface:
    media_obj = Media

    @staticmethod
    def retrieve_media_instance(id):
        result = Media.query.filter_by(id=id).first()
        if result:
            return result
        return ValueError(f"Media with id={id} does not exist")

    @staticmethod
    def get_full_list():
        result = [media.to_dict() for media in Media.query.all()]
        if result:
            return result
        return ValueError("No Media in database")

    @staticmethod
    def create_new_media(media_attributes, returns=False):
        new_instance = Media(title=media_attributes['title'],
                             description=media_attributes['description'],
                             type=media_attributes['type'],
                             file_size=media_attributes['file_size'],
                             popularity=media_attributes['popularity'])
        db.session.add(new_instance)
        db.session.commit()
        if returns != [True, 'instance']:
            return new_instance.to_dict()
        if returns == [True, 'instance']:
            return new_instance

    @staticmethod
    def get_media_by_id(id):
        result = Media.query.filter_by(id=id).first()
        if result:
            return result.to_dict()
        return ValueError(f"Media with id={id} does not exist")

    @staticmethod
    def get_media_by_title(title):
        result = [media.to_public_dict()
                  for media in Media.query.filter_by(title=title).first()]
        if len(result) == 1:
            return result[0]

        elif len(result) > 1:
            return result
        return ValueError(f"Media with title={title} does not exist")

    @staticmethod
    def update_media_by_id(id, values: dict, returns=False):
        result = Media.query.filter_by(id=id).first()
        if result:
            for key, value in values.items():
                if value is not None:
                    setattr(result, key, value)
            db.session.commit()
            if returns:
                return result.to_dict()
        return ValueError(f"Media with id={id} does not exist")

    @staticmethod
    def delete_media_by_id(id):
        result = Media.query.filter_by(id=id).first()
        if result:
            db.session.delete(result)
            db.session.commit()
            return True
        return ValueError(f"Media with id={id} does not exist")

    @staticmethod
    def add_server_to_relational_mapping(media, server, returns=False):
        media.server_list.append(server)
        db.session.commit()
        if returns:
            instance_dict = media.to_dict()
            return {instance_dict['id']: instance_dict['server_list']}

    @staticmethod
    def get_server_ids_for_media(media):
        return media.server_list
