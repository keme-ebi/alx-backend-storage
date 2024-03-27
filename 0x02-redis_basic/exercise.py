#!/usr/bin/env python3
"""
exercise
"""
import redis
import uuid
from typing import Union


class Cache:
    """a Cache class"""

    def __init__(self) -> None:
        """initialization and storing of reids client instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates a random key using uuid, stores the input data
            in Redis using the random key and return the key
        Arg:
            data(any): can be a str, bytes, int or float
        Return:
            the random key generated
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
