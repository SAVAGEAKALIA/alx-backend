#!/usr/bin/env python3
"""Intro to Redis: Basic Tasks """
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    # key = f'{method.__qualname__}_calls'
    key = f'{method.__qualname__}'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper around functions that return method """
        # if not hasattr(self, '__redis'):
        #     self.__redis = redis.Redis()
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Call history method to store history of inputs and outputs"""
    key_input_name = f'{method.__qualname__}:inputs'
    key_output_name = f'{method.__qualname__}:outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper around functions that return method """

        # history = self._redis.lrange(key, 0, -1)
        # print(f"Call history for {key}:")
        # for call in history:
        #     print(call.decode("utf-8"))
        # result = method(self, *args, **kwargs)
        # self._redis.rpush(key, str(result))
        # return result
        self._redis.rpush(key_input_name, str(*args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(key_output_name, result)
        return result

    return wrapper


def replay(method: Callable) -> Callable:
    """Replay the history of all calls made"""
    key_input_name = f'{method.__qualname__}:inputs'
    key_output_name = f'{method.__qualname__}:outputs'
    redis_instance_method = method.__self__._redis

    # get history of method calls
    inputs_history = redis_instance_method.lrange(key_input_name, 0, -1)
    outputs_history = redis_instance_method.lrange(key_output_name, 0, -1)

    # No to iterate and return values from history
    print(f'{method.__qualname__} was called {len(inputs_history)} times:')
    for input_args, output_args in zip(inputs_history, outputs_history):
        val = f'{method.__qualname__}(*{(input_args.decode("utf-8"),)} -> {output_args.decode("utf-8")}'
        print(val)


class Cache:
    """Cache Class that uses Redis"""

    def __init__(self) -> None:
        """Instantiation method for Cache Class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method that takes data argument and return string"""

        random_key_str = str(uuid4())
        self._redis.set(random_key_str, data)
        return random_key_str

    def get(self, key: str, fn=None) -> Union[str, bytes, int, float, None]:
        """Get method that takes key argument and returns data string"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            if fn == int:
                data = self.get_int(data)
            elif callable(fn):
                data = fn(data)
            else:
                data = self.get_str(data)

        # print(data)
        return data

    def get_str(self, data: Union[str, bytes, int, float, None]) -> str:
        """Helper method to convert data to string"""
        if isinstance(data, (str, bytes)):
            return data.decode("utf-8")
        return str(data)

    def get_int(self, data: Union[str, bytes, int, float, None]) -> int:
        """Helper method to convert data to int"""
        return int(data)
