#!/usr/bin/env python3
"""Implement an expiring web cache and tracker"""
import redis
import requests


def get_page(url: str) -> str:
    """Gets the HTML content of a particular URL and return it. Return the
    cached content if recently requested (up to 10 seconds).
    """
    key = "count:{}".format(url)
    r = redis.Redis()
    r.incr(key)
    cache = r.get(url)
    if cache:
        return str(cache)
    else:
        html = requests.get(url).text
        r.set(url, html, ex=10)
        return html
