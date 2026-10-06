import matplotlib.pyplot as plt

subjects = ['Програмування', 'Математика', 'Англійська', 'Інші предмети']
hours = [40, 30, 20, 10]

plt.pie(hours, labels=subjects, autopct='%1.0f%%')

plt.title('Розподіл навчального часу')
plt.savefig("circle.png")
plt.show()
