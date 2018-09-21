"""61070023 EX_pointTriangle"""
from math import sqrt
def main():
    """main func"""
    #Triangle
    point_x1, point_y1 = int(input()), int(input())     #Point1
    point_x2, point_y2 = int(input()), int(input())     #Point2
    point_x3, point_y3 = int(input()), int(input())     #Point3


    #A point in/out/on Triangle
    point_x, point_y = int(input()), int(input())

    #find Triangle line
    line1 = calc1(point_x1, point_y1, point_x2, point_y2)
    line2 = calc1(point_x1, point_y1, point_x3, point_y3)
    line3 = calc1(point_x3, point_y3, point_x2, point_y2)
    
    #Half perimeter Triangle 
    half = (line1+line2+line3)/2

    #find Triangle line <SP>
    l01 = calc1(point_x, point_y, point_x1, point_y1)
    l02 = calc1(point_x, point_y, point_x2, point_y2)
    l03 = calc1(point_x, point_y, point_x3, point_y3)

    #find area special triangle
    tri1 = sqrt(half(half-))




def calc1(num_x1, num_y1, num_x2, num_y2):                  #Find distance between DOT
    result = sqrt((num_y2-num_y1)**2 + (num_x2-num_x1)**2)
    return result

main()

def calc2(num_x1, num_y1, num_x2, num_y2)