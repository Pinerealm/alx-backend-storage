#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://localhost:27017')
    nginx_collection = client.logs.nginx
    num_docs = nginx_collection.count_documents({})
    print(f'{num_docs} logs')

    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        num_methods = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {num_methods}')

    num_path = nginx_collection.count_documents({"path": "/status",
                                                 "method": "GET"})
    print(f'{num_path} status check')
