import math

x = float(input("x? "))

if x > 0:
    # tg(x) + ctg(x)
    fx = math.tan(x) + 1/math.tan(x)
elif x >= -4 and x <= 0:
    # e^(2x+pi) + ln(|x-1|)
    fx = math.exp(2*x + math.pi) + math.log(abs(x - 1))
elif x < -4:
    # cos(x + pi/2 + 0.1)
    fx = math.cos(x + math.pi/2 + 0.1)

print("f(x) =", fx)