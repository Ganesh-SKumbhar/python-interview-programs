# 14. Python Program to Find the vertex, focus, and directrix of a parabola

# The vertex : of a parabola is the coordinate from which it takes the sharpest turn whereas y=a is the straight-line used to generate the curve
# A directrix : a fixed-line used in describing a curve or surface
# Focus : is the point with is equidistant from all points of the parabola.

def parabola(p, q, r):
    print("Vertex of the parabola is (", (-q / (2 * p)), ",", (((4 * p * r) - (q * q)) / (4 * p)), ")")

    print("Focus of the parabola is (", (-q / (2 * p)), ",", (((4 * p * r) - (q * q) + 1) / (4 * p)), ")")

    print("Equation of the directrix is y = ", (int)(r - ((q * q) + 1) * 4 * p))


p = 2
q = 4
r = 6

parabola(p, q, r)

# Vertex of the parabola is ( -1.0 , 4.0 )
# Focus of the parabola is ( -1.0 , 4.125 )
# Equation of the directrix is y =  -130