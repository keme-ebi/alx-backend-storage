#!/usr/bin/env python3
"""
8-all
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection
    Args:
        mongo_collection: collection to go through
    Returns:
        all documents in a collection,
        else an empty list if no document in the collection
    """
    doc = mongo_collection.find({})
    return [] if not doc else doc
