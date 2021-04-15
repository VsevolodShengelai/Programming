import math
import copy

class coord_systems:
    Cartesian = 0
    Polar = 1

class cartesian_coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class polar_coord:
    def __init__(self, radius, angle):
        self.radius = radius
        self.angle = angle

class Point:
    def __init__(self, a1 = 0, a2 = 0, coord_system = coord_systems.Cartesian):
        if type(a1) == str:
            p = a1.find(',') #находим запятую
            self.a1 = float(a1[1 : p])
            self.a2 = float( a1[p+1 : -2])
            self.coord_system = coord_systems.Cartesian
         
            #print('|'+str(a1)+'|'+str(self.a1)+'|'+str(self.a2))
            
        if (type(a1) == int) or (type(a1) == float):
            self.a1, self.a2 = a1, a2
            self.coord_system = coord_system

    def __eq__(p1, p2):
        return (abs(p1.a1 - p2.a1) <= 10**-10) and\
               (abs(p1.a2 - p2.a2) <= 10**-10)

    def __ne__(p1, p2):
        return not (p1 == p2)

    def __repr__(self):
        return "("+str(self.a1)+","+str(self.a2)+")"

    def __str__(self):
        return repr(self)

    def to_cartesian(self, radius, angle):
        return cartesian_coord(
            radius * math.cos(angle), 
            radius * math.sin(angle)
        )

    def to_polar(self, x, y):
        return polar_coord(
            math.hypot(x, y),
            math.atan2(y, x)
        )

    def get_x(self):
        return self.a1 if self.coord_system == coord_systems.Cartesian else self.to_cartesian(self.a1, self.a2).x

    def get_y(self):
        return self.a2 if self.coord_system == coord_systems.Cartesian else self.to_cartesian(self.a1, self.a2).y

    def get_r(self):
        return self.a1 if self.coord_system == coord_systems.Polar else self.to_polar(self.a1, self.a2).r

    def get_angle(self):
        return self.a2 if self.coord_system == coord_systems.Polar else self.to_polar(self.a1, self.a2).angle

    def set_x(self, x):
        if (self.coord_system == coord_systems.Cartesian):
            self.a1 = x
        else:
            coord = self.to_polar(x, self.to_cartesian(self.a1, self.a2).y)
            self.a1 = coord.r
            self.a2 = coord.angle

    def set_y(self, y):
        if (self.coord_system == coord_systems.Cartesian):
            self.a2 = y
        else:
            coord = self.to_polar(self.to_cartesian(self.a1, self.a2).x, y)
            self.a1 = coord.r
            self.a2 = coord.angle

    def set_r(self, radius):
        if (self.coord_system == coord_systems.Polar):
            self.a1 = radius
        else:
            coord = self.to_cartesian(r, self.to_polar(self.a1, self.a2).angle)
            self.a1 = coord.x;
            self.a2 = coord.y;

    def set_angle(self, angle):
        if (self.coord_system == coord_systems.Polar):
            self.a2 = angle;
        else:
            coord = self.to_cartesian(self.to_polar(self.a1, self.a2).radius, angle)
            self.a1 = coord.x
            self.a2 = coord.y

with open('points.txt') as fin:
    original = [Point(p) for p in fin.readline().split(', ')]
  
simulacrum = copy.deepcopy(original)
for p in simulacrum:
    print(p, end='')
    p.set_x(p.get_x() + 10)
    p.set_angle(p.get_angle() + 180*math.pi/180)
    p.set_y(-p.get_y())
    p.set_x(-p.get_x() - 10)
    print(p)
  
print('\nIt works!\n' if simulacrum == original else '\nIt not works!\n')
