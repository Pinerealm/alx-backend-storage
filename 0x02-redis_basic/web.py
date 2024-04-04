#!/usr/bin/env python3
"""Implement an expiring web cache and tracker"""
import redis
import requests
from functools import wraps
from typing import Callable


def count_cache(func: Callable) -> Callable:
    """Tracks calls to get_page and caches results for 10 seconds"""
    @wraps(func)
    def wrapper(url):
        key = f"count:{url}"
        r = redis.Redis()
        cache = r.get(url)
        if cache:
            return cache.decode('utf-8')  # type: ignore
        else:
            html = func(url)
            r.incr(key)
            r.set(url, html, ex=10)
            return html
    return wrapper


@count_cache
def get_page(url: str) -> str:
    """Gets the HTML content of a particular URL and return it. Return the
    cached content if recently requested (up to 10 seconds).
    """
    html = requests.get(url).text
    return html
