import math

x = 2
y = 3

num = math.atan(x/y) - (math.sin(x)**2 + x)**(1/2)

den = x ** 2 + 7 * x * y

res = num / den
print(res)


