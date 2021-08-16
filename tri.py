print("Input lengths of the triangle sides: ")
x = int(input("a: "))
y = int(input("b: "))
z = int(input("c: "))
if x > 10 or y > 10 or z > 10:
    print("Sides should be in the range 1-10")
    exit()
if x < y + z and y < x + z and z < x + y:

    if x == y and y == z:
        print("Equilateral triangle")
    elif x == y or y == z or z == x:
        print("isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("triangle is not formed\nIt's not a triangle")