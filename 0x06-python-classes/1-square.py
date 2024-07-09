#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """
    Simple square class with its size as a field

    Attributes:
        size: size of  a square (1 side)
    """
    def __init__(self, size):
        """ Instance the class Square
        
        Arguments:
            size: the size of every side of the Square
        """
        self.__size = size
