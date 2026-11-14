import math
def R(a, b, c):
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return (a * b * c) / (4 * S)
def R(a, b, c):
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return (a * b * c) / (4 * S)
a = float(input("Введіть сторону a: "))
b = float(input("Введіть сторону b: "))
c = float(input("Введіть сторону c: "))
print("Радіус описаного кола:", round(R(a, b, c), 2))
print("Радіус вписаного кола:", round(r(a, b, c), 2))