#!/usr/bin/env python3
"""
9-insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    Args:
        mongo_collection: pymongo collection object
        kwargs: key-word arguments
    Return:
        the new _id
    """
    post = {}
    for k, v in kwargs.items():
        post[k] = v
    docs = mongo_collection.insert_one(post)
    return docs.inserted_id
