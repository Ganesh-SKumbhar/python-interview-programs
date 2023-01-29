# 12. Python Program to calculate the area of a Tetrahedron
# area of tertrahedron = /3 * (side)2

def area_tetrahedron(side):
    area = (3**0.5)*(side**2)
    return area

side = int(input('Enter side of Tetrahedron: '))
print('Area of Tetrahedron is : ',round(area_tetrahedron(side),2))

# Enter side of Tetrahedron: 20
# Area of Tetrahedron is :  692.82
