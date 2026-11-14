import math
num=int(input("введіть 3-цифрове число"))
a=num//100
b=(num//10)%10
c=num%10
a2 = a**2
c2 = c**2
suma = a2 + c2
print("Сума квадратів", suma)
riz = a2
print("Різниця квадрата", riz)
b3 = b**3
c3 = c**3
suma3 = b3 + c3
print("Сума кубів", suma3)
riz3 = b3 - c3
print("Різниця кубів", riz3)
