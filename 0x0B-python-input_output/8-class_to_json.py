#!/usr/bin/python3
"""Module for function class_to_json"""


def class_to_json(obj):
    """
    Returns the dictionary description
    for JSON serialization of an object
    """
    if hasattr(obj, '__dict__'):
        """
        retrieves a dictionary representation of a Student instance
        """
        return obj.__dict__
