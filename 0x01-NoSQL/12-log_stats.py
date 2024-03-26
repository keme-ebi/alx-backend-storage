#!/usr/bin/env python3
"""
12-log_stats
"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx
num_of_logs = collection.count_documents({})
num_of_get = collection.count_documents({"method": "GET"})
num_of_post = collection.count_documents({"method": "POST"})
num_of_put = collection.count_documents({"method": "PUT"})
num_of_patch = collection.count_documents({"method": "PATCH"})
num_of_delete = collection.count_documents({"method": "DELETE"})
status = collection.count_documents({'method': 'GET', 'path': '/status'})

print("{} logs".format(collection.count_documents({})))
print("Methods:")
print("\tmethod GET: {}".format(num_of_get))
print("\tmethod POST: {}".format(num_of_post))
print("\tmethod PUT: {}".format(num_of_put))
print("\tmethod PATCH: {}".format(num_of_patch))
print("\tmethod DELETE: {}".format(num_of_delete))
print("{} status check".format(status))
