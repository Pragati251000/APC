import math

p1 = (2, 3)
p2 = (5, 6)

distance = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
print("Distance:", distance)

points = [(2, 3), (5, 6), (-4, 7)]

farthest = max(points, key=lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2))
print("Farthest point:", farthest)