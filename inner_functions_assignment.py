# Start Program
"""
Program: inner_function_assignment.py
Author: Paul Thairu
Last date modified: 06/017/2020

Write outer Measurement function that that accepts a list of measurements for a rectangle
and returns a string with perimeter and area calls two inner function area and perimeter.
Area function calculate area of a rectangle or square
Perimeter calculate perimeter of a rectangle or square
"""

# Inner function that calculate area
def area(a_list):
    if len(a_list) == 1:
        side_a = a_list[0]
        res = round(side_a * side_a, 2)
        return side_a * side_a
    if len(a_list) == 2:
        side_a = a_list[0]
        side_b = a_list[1]
        res = round(side_a * side_b, 2)
    return res


# inner function that calculates perimeter
def perimeter(a_list):
    if len(a_list) == 1:
        side_a = a_list[0]
        res = round(4 * side_a, 2)
    if len(a_list) == 2:
        side_a = a_list[0]
        side_b = a_list[1]
        res = round(2 * side_a + 2 * side_b, 2)
    return res

# Out function
def measurements(a_list):
    a = area(a_list)    # area function call
    p = perimeter(a_list)   # perimeter function call
    return "Perimeter = " + str(p) + " Area = " + str(a)  # printing area and perimeter











