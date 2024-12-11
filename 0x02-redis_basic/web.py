#!/usr/bin/env python3
"""Function to test Redis Caching through API"""
import redis
import requests
from functools import wraps
from typing import Callable
from jinja2 import Template
from requests import Response

redis_client = redis.Redis()

key0 = 'http://slowwly.robertomurray.co.uk'
url = f'{key0}'


def cache_function(expiry: int = None):
    """Function to cache the number of times a webpage was accessed"""

    def cache_wrapper(method: Callable) -> Callable:
        """Decorator to cache function results with an expiration time."""

        @wraps(method)
        def wrapper(url: str) -> str:
            """Wrapper function for Cache function"""
            # random_key_str = str(uuid4())
            key1 = 'cache:'
            key2 = 'count:'
            cache_key = f'{key1}{url}'
            count_key = f'{key2}{url}'
            cache_content = redis_client.get(cache_key)
            if cache_content:
                print('Cache content Retrieved')
                return cache_content.decode('utf-8')
            print('Cache unavailable, fetching from source...')

            content = method(url)
            if content.status_code == 200:
                print('Success! Caching the result...')
                # random_key_str = str(uuid4())

                # raw_html = content.text
                #
                # # Use Jinja2 Template to strip HTML tags
                # template = Template("{{ content|striptags }}")
                # plain_text = template.render(content=raw_html)

                redis_client.setex(cache_key, expiry, content.text)
                redis_client.incr(count_key)
                return content.text
                # cache_count(url)
            print(f"Failed to fetch URL. Status code: {content.status_code}")
            return f"Error: {content.status_code}"

        return wrapper

    return cache_wrapper


# def cache_count(method: Callable) -> Callable:
#     """Decorator to count how many times a URL is accessed."""
#     @wraps(method)
#     def wrapper(url: str) -> str:
#         count_key = f'count:{url}'
#         redis_client.incr(count_key)
#         return method(url)
#
#     return wrapper


@cache_function(10)
# @cache_count
def get_page(url: str) -> Response:
    """ Get page Function to test Redis Caching """
    response = requests.get(url)
    return response

# if __name__ == "__main__":
#     test_url = "http://slowwly.robertomurray.co.uk"
#
#     # Simulate multiple requests
#     # Simulate multiple requests
#     print("First Request:")
#     print(get_page(test_url))
#     print(f'cache:{test_url}')
#     print(f"Access count: {redis_client.get(f'count:{test_url}').decode('utf-8')}")
#
#     print("\nSecond Request (Cache Hit):")
#     print(get_page(test_url))
#     print(f'cache:{test_url}')
#     print(f"Access count: {redis_client.get(f'count:{test_url}').decode('utf-8')}")
#
#     print("\nCheck Previous Cache:")
#     cached_content = redis_client.get(f'cache:{test_url}')
#     print(cached_content.decode('utf-8') if cached_content else "No cache found.")
