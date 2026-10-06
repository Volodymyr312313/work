import matplotlib.pyplot as plt
import random

grades = [random.randint(0, 100) for _ in range(50)]

plt.hist(grades, bins=10)

plt.title('Розподіл оцінок з англійської мови')
plt.xlabel('Оцінка')
plt.ylabel('Кількість студентів')
plt.savefig("histogram.png")
plt.show()
