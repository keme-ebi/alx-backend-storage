#!/usr/bin/env python3
"""
11-schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns a list of school having a specific topic
    Args:
        mongo_collection: pymongo collection object
        topic(string): topic to search for
    Return:
        list of school having the specific topic
    """
    school = []
    for to in mongo_collection.find({'topics': topic}):
        school.append(to)
    return school
