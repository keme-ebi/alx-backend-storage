#!/usr/bin/env python3
"""
101-students
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    Args:
        mongo_collection: pymongo collection object
    Return:
        students sorted by average score
    """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return mongo_collection.aggregate(pipeline)
