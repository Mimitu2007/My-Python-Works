import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.2, 10.2, 0.1)

y = np.log(x) * np.cos(x) + np.log10(x) * np.cos(x)

plt.plot(x, y, color='yellow', linestyle='-', label='y = ln(x)cos(x) + lg(x)cos(x)')

plt.xlabel('Вісь X')
plt.ylabel('Вісь Y')
plt.title('Графік функції')
plt.legend()
plt.grid(True)
plt.savefig('triangle.svg')
print("Графік збережено у файл triangle.svg")

plt.show()