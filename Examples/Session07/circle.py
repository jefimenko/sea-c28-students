#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return u'Circle with radius: {radius:.6f}'.format(radius=self.radius)
    def __repr__(self):
        return 'Circle({radius})'.format(radius=self.radius)
    def __add__(self, other):
        return Circle(self.radius+other.radius)
    def __mul__(self, factor):
        return Circle(self.radius*factor)
    def __cmp__(self, other):
        return self.radius - other.radius
    def __ne__(self, other):
        return self.radius - other.radius


    def get_diameter(self):
        return self.radius * 2.0
    def set_diameter(self, diameter=None):
        if diameter:
            self.radius = diameter / 2.0
        else:
            self.diameter = self.radius * 2.0
    diameter = property(get_diameter, set_diameter)
    
    def get_area(self):
        return math.pi * (self.radius**2)
    area = property(get_area)
