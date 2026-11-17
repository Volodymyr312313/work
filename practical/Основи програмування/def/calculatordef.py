import sys

item = []
5+(7+3)
def add_item(name, price):
    item.append((name, price))
    print(f"Товар '{name}' додано")

def total_price():
    return sum(price for name, price in item)

def show_item():
    if not item:
        print("Список порожній")
        return
    for name, price in item:
        print(f"{name}: {price} грн")

def left():
    sys.exit(0)

print("Оберіть цифру 1-4:")
print("1. Додати товар до списку")
print("2. Підрахувати загальну суму")
print("3. Вивести список товарів")
print("4. Вийти")

while True:
    user = input("\nВведіть номер: ")

    if user == "1":
        name = input("Введіть назву товару: ")
        price = float(input("Введіть ціну: "))
        add_item(name, price)

    elif user == "2":
        print("Загальна сума:", total_price())

    elif user == "3":
        show_item()

    elif user == "4":
        left()

    else:
        print("Невірний вибір")
