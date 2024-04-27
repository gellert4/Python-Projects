import math  # import math


def distance(x1, y1, x2, y2):  # def distance
    distance = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
    return distance  # return value


x1 = float(input("Enter x1: "))  # inputs
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

A = distance(x1, y1, x2, y2)  # calculate

print("The distance between (", float(x1), ",", float(y1),
      ") and ( ", float(x2), ",", float(y2), ") is ", round(float(A), 3))
