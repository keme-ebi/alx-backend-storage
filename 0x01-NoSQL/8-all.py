#!/usr/bin/env python3
"""
8-all
"""
import pymongo
from pymongo.collection import Collection
from typing import List


def list_all(mongo_collection: Collection) -> List:
    """
    lists all documents in a collection
    Args:
        mongo_collection: collection to go through
    Returns:
        all documents in a collection,
        else an empty list if no document in the collection
    """
    coll_list = []
    for coll in mongo_collection.find({}):
        coll_list.append(coll)

    return coll_list
