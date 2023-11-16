import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# sqrt - square root - pierwiastek
segment_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

circle_area = math.pi * (segment_length / 2)**2

radius = segment_length / 2

print("Circle area:", circle_area)
print("Radius:", radius)