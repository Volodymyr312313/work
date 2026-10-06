shopping_list = []

while True:
    print("\n---------------------")
    print("--Список покупок--")
    print("1. Додати товар")
    print("2. Видалити товар")
    print("3. Показати список")
    print("4. Вийти")
    print("---------------------")

    user = input("Оберіть цифру: ").strip()

    if user == "1":
        item = input("Введи товар, який хочеш додати? ").strip()
        if item:
            shopping_list.append(item)
            print(f"Товар '{item}' додано до списку")
        else:
            print("Назва товару не може бути порожньою")

    elif user == "2":
        item = input("Який товар ви бажаєте видалити? ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Товар '{item}' видалено!")
        else:
            print("Такого товару немає у списку")

    elif user == "3":
        print("--Ваш список покупок--")
        if not shopping_list:
            print("Ваш список порожній.")
        else:
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")

    elif user == "4":
        break

    else:
        print("Такого вибору не існує. Оберіть цифру від 1 до 4")
