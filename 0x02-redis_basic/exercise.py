#!/usr/bin/env python3
"""Redis in Python"""
import redis
from typing import Union
from uuid import uuid4
from functools import wraps

Redis_type = Union[str, bytes, int, float]


def count_calls(method: callable) -> callable:
    """Count the number of times a method is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: callable) -> callable:
    """Store the history of inputs and outputs for a particular function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function
        """
        key = method.__qualname__
        input = str(args)
        self._redis.rpush("{}:inputs".format(key), input)
        output = str(method(self, *args, **kwargs))

        self._redis.rpush("{}:outputs".format(key), output)
        return output
    return wrapper


def replay(method: callable) -> None:
    """Display the history of calls of a particular function
    """
    r = redis.Redis()
    key = method.__qualname__
    count = r.get(key).decode("utf-8")
    inputs = r.lrange("{}:inputs".format(key), 0, -1)
    outputs = r.lrange("{}:outputs".format(key), 0, -1)

    print("{} was called {} times:".format(key, count))
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(key, i.decode("utf-8"),
                                     o.decode("utf-8")))


class Cache:
    """The Cache class
    """
    def __init__(self):
        """Initialize a Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Redis_type) -> str:
        """Generate a random key, store the input data in Redis using the key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None) -> bytes:
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
