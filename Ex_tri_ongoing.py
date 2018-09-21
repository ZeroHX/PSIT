"""61070023 Ex_Triangle ver2.5"""
from math import sqrt
def main():
    """main func"""
     #Triangle
    point_x1, point_y1 = int(input()), int(input())     #Point1
    point_x2, point_y2 = int(input()), int(input())     #Point2
    point_x3, point_y3 = int(input()), int(input())     #Point3

    #A point in/out/on Triangle
    point_x, point_y = int(input()), int(input())

    #Find Special Triangle area
    tri1 = abs(point_x*(point_y2-point_y3)+x2*(y3-y1)+x3*(y1-y2))/2.0

def calc(num_x1, num_y1, num_x2, num_y2):
    """This Func calculate distance between Dot"""
    result = sqrt()