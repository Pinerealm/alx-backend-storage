#!/usr/bin/env python3
"""Implement an expiring web cache and tracker"""
import redis
import requests


def get_page(url: str) -> str:
    """Get the HTML content of a particular URL and return it
    """
    key = "count:{}".format(url)
    r = redis.Redis()
    r.incr(key)
    cache = r.get(url)
    if cache:
        return cache.decode("utf-8")
    else:
        html = requests.get(url).text
        r.set(url, html, ex=10)
        return html
