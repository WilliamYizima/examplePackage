# -*- coding: utf-8 -*-

"""
examplePackage.core
~~~~~~~~~~~~
This module implements the abstraction to create the serializer.
"""

from .TargetService import TargetService

class TargetServiceBuilder:
    def __call__(self, status, event, created_at, **_ignored):
        return TargetService(status, event,created_at)
