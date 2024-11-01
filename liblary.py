# Списки для хранения данных
books = []
users = []

# Добавление
def add_book(title, author):
    book = {
        'id': len(books) + 1,
        'title': title,
        'author': author,
        'available': True
    }
    books.append(book)
    print(f"Книга '{title}' добавлена.")

# Регистрация
def add_user(name):
    user = {
        'id': len(users) + 1,
        'name': name
    }
    users.append(user)
    print(f"Пользователь '{name}' зарегистрирован.")

# Поиск
def search_books(query):
    results = [book for book in books if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
    if results:
        for book in results:
            status = "Доступна" if book['available'] else "Выдана"
            print(f"{book['id']}. {book['title']} - {book['author']} ({status})")
    else:
        print("Книги не найдены.")

# Выдача
def issue_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book and book['available']:
        book['available'] = False
        print(f"Книга '{book['title']}' выдана.")
    else:
        print("Книга недоступна для выдачи.")

# Возврат
def return_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book and not book['available']:
        book['available'] = True
        print(f"Книга '{book['title']}' возвращена.")
    else:
        print("Эта книга не была выдана.")

# меню
def main():
    while True:
        print("\nМеню библиотеки:")
        print("1. Добавить книгу")
        print("2. Зарегистрировать пользователя")
        print("3. Поиск книги")
        print("4. Выдать книгу")
        print("5. Вернуть книгу")
        print("6. Выйти")
        
        choice = input("Выберите опцию: ")
        
        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора: ")
            add_book(title, author)
        
        elif choice == '2':
            name = input("Введите имя пользователя: ")
            add_user(name)
        
        elif choice == '3':
            query = input("Введите название или автора для поиска: ")
            search_books(query)
        
        elif choice == '4':
            book_id = int(input("Введите ID книги для выдачи: "))
            issue_book(book_id)
        
        elif choice == '5':
            book_id = int(input("Введите ID книги для возврата: "))
            return_book(book_id)
        
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == '__main__':
    main()
