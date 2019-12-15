#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """ Valide values
            Args:
                width(int): rectangule width
                height(int): rectangule height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calcule rectangule area
            Args:
                width: value integer
                height: value integer
            Return:
                Area(int): width * height
        """
        return "{}".format(self.__width * self.__height)

    def __str__(self):
        """ Return values of width and height
           Args:
                width: value integer
                height: value integer
            Return:
                Rectangule area
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
