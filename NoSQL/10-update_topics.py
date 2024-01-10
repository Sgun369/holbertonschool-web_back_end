#!/usr/bin/env python3
""" Change school topics"""


def update_topiics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    return mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}})
