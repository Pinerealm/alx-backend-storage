#!/usr/bin/env python3
"""Writing strings to Redis in Python"""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """The Cache class
    """
    def __init__(self):
        """Initialize a Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key, store the input data in Redis using the key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
