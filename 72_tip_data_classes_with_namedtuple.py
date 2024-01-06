from collections import namedtuple
# In Java, we create data classes - only getter, setter constructor
# In python we can create such classes using namedtuple

Point = namedtuple('Point', ['x', 'y'])
point1 = Point(1, 2)
print(point1.x)
print(point1.y)
print("----------------------------------------------------------")
ThreeDPoint = namedtuple('ThreeDPoint', ['x', 'y', 'z'])
point2 = ThreeDPoint(3, 4, 5)
print(point2.x)
print(point2.y)
print(point2.z)
print("----------------------------------------------------------")

