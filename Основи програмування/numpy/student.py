import numpy as np

grades = np.random.randint(0, 101, size=(100, 3))

average = np.mean(grades, axis=1).reshape(-1, 1)

print(f"Оцінки студентів {grades} :")

print("Середній бал кожного студента:")
print(average)
