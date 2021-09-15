# -*- coding: utf-8 -*-

"""
examplePackage.core
~~~~~~~~~~~~
This module implements the abstraction to create the serializer.
"""

class SerializerFactory:
    """comment this class"""
    def __init__(self):
        """Create empty dict"""
        self._builders = {}
    
    def register(self, key, builder):
        """"""
        self._builders[key] = builder
        return self._builders

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)