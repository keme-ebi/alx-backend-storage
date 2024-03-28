#!/usr/bin/env python3
"""
exercise
"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable]
            ) -> Union[str, bytes, int, float]:
        """
        gets the data stored in a key using the callable fn
            to convert the data back to the desired format
        Args:
            key(str): key to get data from
            fn: callable to convert the data back to the desired format
        Return:
            converted data
        """
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        returns data from redis in str format
        Arg:
            key(str): key to get data from
        Return:
            data in str format
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        returns data from redis in int format
        Arg:
            key(str): key to get data from
        Return:
            data in int format
        """
        return self.get(key, lambda d: int(d))
