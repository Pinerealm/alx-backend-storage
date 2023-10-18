#!/usr/bin/env python3
"""Writing strings to Redis in Python"""
import redis
from typing import Union
from uuid import uuid4

Redis_type = Union[str, bytes, int, float]


class Cache:
    """The Cache class
    """
    def __init__(self):
        """Initialize a Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Redis_type) -> str:
        """Generate a random key, store the input data in Redis using the key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None) -> Redis_type:
        """Get the value stored in Redis for a given key
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Convert bytes to string
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Convert bytes to int
        """
        return self.get(key, int)
