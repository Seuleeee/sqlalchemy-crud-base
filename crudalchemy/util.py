from sqlalchemy.inspection import inspect
from typing import Type, TypeVar


T = TypeVar("T")


def _serialize_item(model: Type[T]):
    """ Serializer for SQLAlchemy Model Instance """
    return {c.key: getattr(model, c.key) for c in inspect(model).mapper.column_attrs}


def serialize(data):
    """ Serializer for Single or Multiple Model Instance """
    if isinstance(data, list):
        return [_serialize_item(item) for item in data]
    return _serialize_item(data)

