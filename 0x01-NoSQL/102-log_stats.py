#!/usr/bin/env python3
"""Log stats - new version"""
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
    print('IPs:')
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    ip_stats = nginx_collection.aggregate(pipeline)
    for ip_stat in ip_stats:
        print(f'\t{ip_stat.get("_id")}: {ip_stat.get("count")}')
