# 13. Python Program to Find the perimeter of a cylinder
# perimeter of cylinder = 4 * pi * radius + 2 * height
from math import pi
def cylinder_perimeter(radius,height):
    perimeter = 4 * pi * radius + 2 * height
    return perimeter

radius, height = map(int,input('Enter Radius and Height of cylinder separated by space : ').split())
print(f'Perimeter of cylinder with radius: {radius} and height: {height} is : ', cylinder_perimeter(radius,height))

# Enter Radius and Height of cylinder separated by space : 10 20
# Perimeter of cylinder with radius: 10 and height: 20 is :  165.66370614359172
