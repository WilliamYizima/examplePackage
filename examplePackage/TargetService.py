# -*- coding: utf-8 -*-

"""
examplePackage.core
~~~~~~~~~~~~
This module implements the abstraction to create the serializer.
"""

import json

class TargetService:
    """payload mapping to target service"""
    def __init__(self, status, event, created_at):
        self._status = status
        self._event = event
        self._created_at = created_at

    def serializer(self,payload):
        r_dict = {}
        r_dict['status'] = payload[self._status]
        r_dict['event'] = payload[self._event]
        r_dict['created_at'] = payload[self._created_at]
        return json.dumps(r_dict, indent=4)