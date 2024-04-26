import math


def my_map(func, list1, list2):
    return [func(point1, point2) for point1, point2 in zip(list1, list2)]

def calc_distance(point1, point2):
    # Extraction des coordonnées des points
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    # Calcul de la distance entre les points
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    
    return distance

points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]
distances = my_map(calc_distance, points1, points2)
print(distances)
