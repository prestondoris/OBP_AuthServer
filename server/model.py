from flask import current_app
from google.cloud import datastore

builtin_list = list

def init_app(app):
    pass

def get_client():
    return datastore.Client(current_app.config['PROJECT_ID'])

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        {id: id, prop: val, ...}
    """
    if not entity:
        return None
    if isinstance(entity, builtin_list):
        entity = entity.pop()

    entity['id'] = entity.key.id 
    return entity

def read(key):
    ds=get_client()
    key = ds.key('User', key)
    entity = ds.get(key)
    return from_datastore(entity)

def update(data, key=None):
    ds = get_client()
    key = ds.key('User', key)

    entity = datastore.Entity(key=key)

    entity.update(data)
    ds.put(entity)
    return from_datastore(entity)

create = update

def delete(key):
    ds = get_client()
    key = ds.key('User', key)
    ds.delete(key)
