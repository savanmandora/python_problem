import math
import random

"""
what we need,
circle radius
circle area = pie * r_sqr_2
square area = 4 * r_sqr_2

steps,
generate random points within square
count how many fall in enclosed circle and in square
4 * number of points in circle / total points
"""

def get_distance(a,b):
    return math.sqrt(math.pow((a[0] - a[1]),2) + math.pow((b[0] - b[1]),2))

def generate_points(area):
    """
    generate random points inside of square
    """
    max_points = 1000
    points = []

    for i in range(max_points):
        points.append([random.randrange(1,area),random.randrange(1,area)])

    return points

def diff_points(points,circle_area):
    """
    spliting points on the basis of on what it is generated i.e. circle, square
    """
    circle_points = []
    square_points = []

    for i in points:
        dis = get_distance([0,0],i)

        if dis <= circle_area:
            circle_points.append(i)
        else:
            square_points.append(i)

    return circle_points, square_points

def estimate_pie(circle_points,square_points):
    """
    calculating entimated pie
    """
    return 4 * (len(circle_points) / (len(circle_points) + len(square_points)))

if __name__ == "__main__":
    circle_rad = float(input("Circle radius: "))

    circle_area = 3.14 * math.pow(circle_rad, 2)
    square_area = 4 * math.pow(circle_rad, 2)

    points = generate_points(square_area)

    cir_points, sqr_points = diff_points(points,circle_area)
    
    estimated_pie = estimate_pie(cir_points,sqr_points)
    print(estimated_pie)
     
    # print(f"Circle points: {cir_points} \nSquare points: {sqr_points}")
    