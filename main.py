from library_manager import LibraryManager

def main():
    library = LibraryManager()
    
    # Начальное формирование данных
    initial_books = [
        {"udk": "001.1", "author": "Иванов И.И.", "title": "Основы программирования", "year": 2020, "quantity": 5},
        {"udk": "002.2", "author": "Петров П.П.", "title": "Алгоритмы и структуры данных", "year": 2019, "quantity": 3},
        {"udk": "003.3", "author": "Сидоров С.С.", "title": "Базы данных", "year": 2021, "quantity": 4}
    ]
    
    for book in initial_books:
        library.add_book(book)
    
    # Демонстрация работы
    while True:
        print("\n=== Система управления библиотекой ===")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Показать все книги (по годам)")
        print("4. Найти книгу")
        print("5. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            add_book_interactive(library)
        elif choice == "2":
            remove_book_interactive(library)
        elif choice == "3":
            library.display_books_by_year()
        elif choice == "4":
            search_book_interactive(library)
        elif choice == "5":
            break
        else:
            print("Неверный выбор!")

def add_book_interactive(library):
    print("\n--- Добавление книги ---")
    try:
        udk = input("УДК: ")
        author = input("Автор: ")
        title = input("Название: ")
        year = int(input("Год издания: "))
        quantity = int(input("Количество: "))
        
        book_data = {
            "udk": udk,
            "author": author,
            "title": title,
            "year": year,
            "quantity": quantity
        }
        
        library.add_book(book_data)
        print("Книга успешно добавлена!")
    except ValueError:
        print("Ошибка ввода данных!")

def remove_book_interactive(library):
    print("\n--- Удаление книги ---")
    udk = input("Введите УДК книги для удаления: ")
    library.remove_book(udk)

def search_book_interactive(library):
    print("\n--- Поиск книги ---")
    udk = input("Введите УДК для поиска: ")
    library.find_book(udk)

if __name__ == "__main__":
    main()