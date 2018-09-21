"""61070023 EX_pointTriangle"""
from math import sqrt
def main():
    """main func"""
    #Triangle
    point_x1, point_y1 = int(input()), int(input())     #Point1
    point_x2, point_y2 = int(input()), int(input())     #Point2
    point_x3, point_y3 = int(input()), int(input())     #Point3

    #A point in/out Triangle
    point_x, point_y = int(input()), int(input())

    #find Triangle line
    line1 = calc(point_x1, point_y1, point_x2, point_y2)
    line2 = calc(point_x1, point_y1, point_x3, point_y3)
    line3 = calc(point_x3, point_y3, point_x2, point_y2)

    #Check in Triangle
    if line1-calc(point_x, point_y, point_x1, point_y1) > 0 \
    and line2-calc(point_x, point_y, point_x1, point_y1) > 0 \
    and line3-calc(point_x, point_y, point_x2, point_y2) > 0:
        print("in")

    #Check out Triangle
    elif  line1-calc(point_x, point_y, point_x1, point_y1) < 0 \
    and line2-calc(point_x, point_y, point_x1, point_y1) < 0 \
    and line3-calc(point_x, point_y, point_x2, point_y2) < 0:
        print("out")

    #Check on Triangle
    else:
        print("on")

def calc(num_x1, num_y1, num_x2, num_y2):
    result = sqrt((num_y2-num_y1)**2 + (num_x2-num_x1)**2)
    return result

main()
