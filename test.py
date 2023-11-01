import unittest
@teskbook ("NGC3.ipynb", execute = 0)
class lbrcatalogtest(unittest.TestCase):
    def setup(self):
        self.catalog = lbr_catalog()
        self.book1 = book("Title 1", "Author 1", 2)
        self.book2 = book("Title 2", "Author 2", 3)
        self.book3 = book("Title 3", "Author 3", 4)
        self.catalog.add_book(self.book1)
        self.catalog.add_book(self.book2)
        self.catalog.add_book(self.book3)
    def test_add_book(self):
        new_book = Book("New Book", "New Author",5)
        self.catalog.add_book(new_book)
        self.assertIn(new_book, self.catalog.book)
    def test_add_invalid_book(self):
        with self.assertRaises(ValueError):
            self.catalog.add_book("Invalid book object")
    def test_search_book_by_title(self):
        result = self.catalog,search_books("title")
        self.asserEqual(len(result, 3))
        self.asserIn(self.book1, result)
        self.asserIn(self.book2, result)
        self.asserIn(self.book3, result)
    def test_search_book_by_title(self):
        result = self.catalog,search_books("author")
        self.asserEqual(len(result, 3))
        self.asserIn(self.book1, result)
        self.asserIn(self.book2, result)
        self.asserIn(self.book3, result)
    def test_remove_book(self):
        self.catalog.remove_book(self.book2)
        self.asserNotIn(self.book2, self.catalog.books)
        self.assertIn(self.book1,self.catalog.books)

if __name__ == '__main__':
    unittest.main()

        
        
    

