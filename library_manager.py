class BookNode:
    def __init__(self, book_data):
        self.udk = book_data["udk"]
        self.author = book_data["author"]
        self.title = book_data["title"]
        self.year = book_data["year"]
        self.quantity = book_data["quantity"]
        self.left = None
        self.right = None

class LibraryManager:
    def __init__(self):
        self.root = None
    
    def add_book(self, book_data):
        new_node = BookNode(book_data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_node(self.root, new_node)
    
    def _insert_node(self, current, new_node):
        if new_node.udk < current.udk:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_node(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_node(current.right, new_node)
    
    def remove_book(self, udk):
        self.root = self._remove_node(self.root, udk)
    
    def _remove_node(self, node, udk):
        if node is None:
            print(f"Книга с УДК {udk} не найдена!")
            return None
        
        if udk < node.udk:
            node.left = self._remove_node(node.left, udk)
        elif udk > node.udk:
            node.right = self._remove_node(node.right, udk)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            min_larger_node = self._find_min(node.right)
            node.udk = min_larger_node.udk
            node.author = min_larger_node.author
            node.title = min_larger_node.title
            node.year = min_larger_node.year
            node.quantity = min_larger_node.quantity
            node.right = self._remove_node(node.right, min_larger_node.udk)
        
        return node
    
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def find_book(self, udk):
        result = self._search_node(self.root, udk)
        if result:
            self._print_book_info(result)
        else:
            print(f"Книга с УДК {udk} не найдена!")
        return result
    
    def _search_node(self, node, udk):
        if node is None or node.udk == udk:
            return node
        
        if udk < node.udk:
            return self._search_node(node.left, udk)
        else:
            return self._search_node(node.right, udk)
    
    def display_books_by_year(self):
        books = self._collect_all_books(self.root)
        books_sorted = sorted(books, key=lambda x: x["year"])
        
        print("\n--- Список книг по годам издания ---")
        for book in books_sorted:
            print(f"УДК: {book['udk']}, Автор: {book['author']}, "
                  f"Название: {book['title']}, Год: {book['year']}, "
                  f"Кол-во: {book['quantity']}")
    
    def _collect_all_books(self, node):
        books = []
        if node:
            books.append({
                "udk": node.udk,
                "author": node.author,
                "title": node.title,
                "year": node.year,
                "quantity": node.quantity
            })
            books.extend(self._collect_all_books(node.left))
            books.extend(self._collect_all_books(node.right))
        return books
    
    def _print_book_info(self, book_node):
        print(f"\n--- Информация о книге ---")
        print(f"УДК: {book_node.udk}")
        print(f"Автор: {book_node.author}")
        print(f"Название: {book_node.title}")
        print(f"Год издания: {book_node.year}")
        print(f"Количество: {book_node.quantity}")