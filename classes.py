import math
import pygame


class Individual:
    def __init__(self):
        self.springs = [

        ]

class Spring:
    def __init__(self, prefered_length: int | float, strength: int | float, node1, node2):
        """
        prefered_length: the length at witch the spring is at rest
        strength: the srength of the spring in Newtons
        """
        self.prefered_length = prefered_length
        self.strength = strength
        self.node1: Node = node1
        self.node2: Node = node2
    
        self.node1_force_id = None
        self.node2_force_id = None

    def length(self):
        return (self.node1.pos - self.node2.pos).mag()

    def displacment(self):
        return self.length() - self.prefered_length 

    def force(self):
        return -(self.strength * self.length())
    
    def display(self):
        ...
    
    def update(self):
        self.node1.force(self.force(), self.node1_force_id)
        self.node2.force(self.force(), self.node2_force_id)

class Node:
    def __init__(self, pos):
        self.pos = pos

        self.vel = Vec2()
    
        self.forces =  {}

        self.t = 0

    def update(self, t):
        acc = Vec2()

        for key in self.forces:
            force = self.forces[key]
            acc += force

        delta = t - self.t

        self.vel += acc * delta

        self.pos += self.vel

        self.t = t

    def force(self, force, id=None):
        if not id:
            id = 0
            while id in self.forces.keys():
                id += 1
        
        self.forces[id] = force

        return id

class Vec2:
    def __init__(self, x: int | float=0, y: int | float=0):
        self.x = x
        self.y = y
    
    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def __add__(self, other):
        if type(other) == Vec2:
            return Vec2(self.x + other.x, self.y + other.y)
        
        if type(other) in [int, float]:
            return Vec2(self.x + other, self.y + other)
        
    def __sub__(self, other):
        if type(other) == Vec2:
            return Vec2(self.x - other.x, self.y - other.y)
        
        if type(other) in [int, float]:
            return Vec2(self.x - other, self.y - other)
    
    def __add__(self, other):
        if type(other) == Vec2:
            return self.x * other.x + self.y * other.y
        
        if type(other) in [int, float]:
            return Vec2(self.x * other, self.y * other)
        
    def __truediv__(self, other: int | float):
        return Vec2(self.x / other, self.y / other)
    
    def unit(self):
        return self / self.mag()