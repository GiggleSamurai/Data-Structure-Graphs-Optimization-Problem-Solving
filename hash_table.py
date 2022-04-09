"""
Author: Louis Wong
ID: #009457081
E-Mail: lwong33@wgu.edu
Project: C950
Version: 2
File: hash_table.py
"""
class HashTable:
    # Create A Table
    def __init__(self, hash_table_size):
        self.len = hash_table_size
        self.hashtable = []
        for i in range(hash_table_size):
            self.hashtable += [[]]

    # Insert to Table
    def insert(self, item):
        # item must be in this format: item [key,value 1, value 2,..etc]
        bucket = hash(item[0]) % self.len
        self.hashtable[bucket] += [item]

    # Lookup Exiting Item
    def lookup(self, key):
        bucket = hash(key) % self.len
        bucket_list = self.hashtable[bucket]
        for item in bucket_list:
            if item[0] == key:
                return item
        return None

    # Remove Exiting Item
    def remove(self, key):
        bucket = hash(key) % self.len
        bucket_list = self.hashtable[bucket]
        for item in bucket_list:
            if item[0] == key:
                bucket_list.remove(item)

    # Update Exiting Item
    def update(self, key, item):
        self.remove(key)
        self.insert(item)