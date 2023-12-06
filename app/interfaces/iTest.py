from ..models import TestBool
from ..ext.database import DB as db


class TestInterface:

    @staticmethod
    def get_full_list():
        result = [test_bool.to_dict() for test_bool in TestBool.query.all()]
        if result:
            return result
        return ValueError("No TestBool in database")

    @staticmethod
    def get_by_id(id):
        result = TestBool.query.filter_by(id).first()
        if result:
            return result.to_dict()
        return ValueError(f"TestBool with id={id} does not exist")

    @staticmethod
    def get_all_true():
        result = [test_bool.to_dict()
                  for test_bool in TestBool.query.filter_by(bool=True).all()]
        if result:
            return result
        return ValueError("No TestBool with bool=True")

    @staticmethod
    def add_data_to_table(value=True, returns=False):
        new_instance = TestBool(bool=value)
        db.session.add(new_instance)
        db.session.commit()
        if returns:
            return new_instance.to_dict()

    @staticmethod
    def switch_bool_by_id(id, returns=False):
        result = TestBool.query.get(id)
        if result:
            result.bool = not result.bool
            db.session.commit()
            if returns:
                return result.to_dict()
        return ValueError(f"TestBool with id={id} does not exist")

    def delete_row_by_id(id):
        result = TestBool.query.get(id)
        if result:
            db.session.delete(result)
            db.session.commit()
            return True
        return ValueError(f"TestBool with id={id} does not exist")
