import sys
import math

a1 = float(sys.argv[1])
b1 = float(sys.argv[2])
a2 = float(sys.argv[3])
b2 = float(sys.argv[4])
h  = float(sys.argv[5])

S1 = a1 * b1
S2 = a2 * b2
V = (h / 3) * (S1 + S2 + math.sqrt(S1 * S2))
l1 = math.sqrt(h**2 + ((a1 - a2) / 2)**2)
l2 = math.sqrt(h**2 + ((b1 - b2) / 2)**2)
Sb = ((a1 + a2) * l2) + ((b1 + b2) * l1)

print(S1)
print(S2)
print(Sb)
print(V)