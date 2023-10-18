#!/usr/bin/env python3
"""List schools by topic"""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools that have a specific topic
    """
    return mongo_collection.find({"topics": topic})
