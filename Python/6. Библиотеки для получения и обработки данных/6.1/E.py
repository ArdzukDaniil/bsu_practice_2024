import math

x, y = map(float, input().split())
rho, phi = map(float, input().split())
x_pole = rho * math.cos(phi)
y_pole = rho * math.sin(phi)
distance = math.sqrt((x - x_pole)**2 + (y - y_pole)**2)
print(distance)