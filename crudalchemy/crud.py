from typing import Type, TypeVar, Union, Any
from typing import Generic

from sqlalchemy.orm import Session


T = TypeVar("T")


class CRUDBase(Generic[T]):
    def __init__(self, model: Type[T]):
        """
        CRUD object with methods for Create, Read, Update, Delete.
        :param model: SQLAlchemy model class
        """
        self.model = model

    def create(self, db: Session, obj_in: T) -> T:
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        return obj_in

    # TODO: pk를 어떻게 불러올 것인지?
    def get(self, db: Session, pk: int) -> T:
        return db.query(self.model).filter(self.model.id == pk).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> list[T]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def update(self, db: Session, db_obj: T, obj_in: Union[dict, Any]) -> T:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.__dict__
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return obj_in

    def remove(self, db: Session, id: int) -> T:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj

