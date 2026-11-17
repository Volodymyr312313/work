import matplotlib.pyplot as plt

students = ['Олена', 'Андрій', 'Марія', 'Максим', 'Софія', 'Денис', 'Анна']
grades = [88, 92, 75, 85, 96, 78, 90]

colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow', 'pink']

plt.bar(students, grades, color=colors)

plt.title('Середні оцінки студентів з математики')
plt.xlabel('Студенти')
plt.ylabel('Оцінка')
plt.show()
