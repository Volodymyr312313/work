import matplotlib.pyplot as plt

students = ['Олена', 'Андрій', 'Марія', 'Максим', 'Софія', 'Денис', 'Анна']
grades = [88, 92, 75, 85, 96, 78, 90]

plt.figure(figsize=(10, 5))

plt.plot(students, grades, marker='o', label='Середній бал')

plt.title('Середні оцінки студентів з програмування')
plt.xlabel('Студенти')
plt.ylabel('Оцінка (бали)')

plt.grid()
plt.legend()
plt.show()
