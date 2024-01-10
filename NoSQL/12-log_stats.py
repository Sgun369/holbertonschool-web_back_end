#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


def get_nginx_stats(mongo_collection):
    """ provides some stats about Nginx logs stored in MongoDB"""
    total_logs = mongo_collection.count_documents({})

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in http_methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_logs_count = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_logs_count} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    get_nginx_stats(nginx_collection)
