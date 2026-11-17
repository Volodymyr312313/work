import json

config = "books.json"


def load_books():
    try:
        with open(config, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_books(books):
    with open(config, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


books = load_books()

while True:
    print("\n1. Додати книгу")
    print("2. Видалити книгу")
    print("3. Показати всі книги")
    print("4. Вийти")

    choice = input("Виберіть дію: ")

    if choice == "1":
        title = input("Назва: ")
        author = input("Автор: ")
        year = input("Рік: ")

        books.append({
            "назва": title,
            "автор": author,
            "рік": year
        })

        save_books(books)
        print("Книгу додано!")

    elif choice == "2":
        title = input("Введіть назву книги: ")

        books = [book for book in books if book["назва"] != title]

        save_books(books)
        print("Книгу видалено!")

    elif choice == "3":
        if not books:
            print("Колекція порожня.")
        else:
            for book in books:
                print(f'{book["назва"]} — {book["автор"]}, {book["рік"]}')

    elif choice == "4":
        break

    else:
        print("Невірний вибір.")
