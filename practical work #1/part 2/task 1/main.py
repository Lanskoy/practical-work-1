import math

u = 0
v = 0

s = 2 * u
x = u * v

num = math.sin(2*x) + 3 * math.exp(-s)

den = 1 + math.atan(4 * x)**2

res = num / den
print (res)