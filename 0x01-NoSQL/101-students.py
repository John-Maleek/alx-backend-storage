#!/usr/bin/env python3
"""
    a Python function that returns all
    students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$scores.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    results = list(mongo_collection.aggregate(pipeline))

    return results
