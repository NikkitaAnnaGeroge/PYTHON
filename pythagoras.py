from operator import truediv


def is_right_angle_triangle(side1,side2,side3):
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        return True
    return False

side1=int(input("enter the side 1 of triangle:"))
side2=int(input("enter the side  2 of  triangle:"))
side3=int(input("enter the side 3 of triangle:"))
if is_right_angle_triangle (side1,side2,side3):
    print(f"The given sides are part of right angle triangle ")
else:
    print(f"The given sides are not part of right angle triangle")
is_right_angle_triangle(side1,side2,side3)