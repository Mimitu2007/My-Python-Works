a = int(input("5"))
b = int(input("1"))
c = int(input("7"))

digits = [a, b, c]
digits.sort()

result = int("".join([str(d)*2 for d in digits]))

print("115577", result)