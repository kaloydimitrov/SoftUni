from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def test_init(self):
        bs = Bookstore(100)
        self.assertEqual(bs.books_limit, 100)
        self.assertEqual(bs.availability_in_store_by_book_titles, {})

    def test_prop(self):
        bs = Bookstore(100)
        bs.availability_in_store_by_book_titles = {"Book1": 30, "Book2": 20}
        bs.sell_book("Book1", 10)
        bs.sell_book("Book2", 10)
        self.assertEqual(bs.total_sold_books, 20)

        self.assertDictEqual(bs.availability_in_store_by_book_titles, {"Book1": 20, "Book2": 10})

    def test_books_limit_error(self):
        with self.assertRaises(Exception) as ex:
            bs = Bookstore(-1)
        self.assertEqual(str(ex.exception), "Books limit of -1 is not valid")

        with self.assertRaises(Exception) as ex:
            bs = Bookstore(0)
        self.assertEqual(str(ex.exception), "Books limit of 0 is not valid")

    def test_magic_len(self):
        bs = Bookstore(100)
        bs.availability_in_store_by_book_titles = {"Book1": 10, "Book2": 10, "Book3": 30}
        self.assertEqual(len(bs), 50)

    def test_receive_book_error(self):
        bs = Bookstore(1)
        bs.availability_in_store_by_book_titles = {"Book1": 10, "Book2": 10}
        with self.assertRaises(Exception) as ex:
            bs.receive_book("b1", 1)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_book_case_one(self):
        bs = Bookstore(100)
        bs.availability_in_store_by_book_titles = {"Book1": 10}
        self.assertEqual(bs.receive_book("Book2", 20), "20 copies of Book2 are available in the bookstore.")
        self.assertDictEqual(bs.availability_in_store_by_book_titles, {"Book1": 10, "Book2": 20})

    def test_receive_book_case_two(self):
        bs = Bookstore(100)
        bs.availability_in_store_by_book_titles = {"Book1": 10, "Book2": 20}
        self.assertEqual(bs.receive_book("Book2", 20), "40 copies of Book2 are available in the bookstore.")
        self.assertDictEqual(bs.availability_in_store_by_book_titles, {"Book1": 10, "Book2": 40})

    def test_sell_book_error_one(self):
        bs = Bookstore(100)
        bs.availability_in_store_by_book_titles = {"Book2": 10, "Book3": 15}
        with self.assertRaises(Exception) as ex:
            bs.sell_book("Book1", 20)
        self.assertEqual(str(ex.exception), "Book Book1 doesn't exist!")

        self.assertEqual(bs.total_sold_books, 0)

    def test_sell_book_error_two(self):
        bs = Bookstore(100)
        bs.availability_in_store_by_book_titles = {"Book1": 15, "Book3": 10, "Book4": 100}
        with self.assertRaises(Exception) as ex:
            bs.sell_book("Book1", 30)
        self.assertEqual(str(ex.exception), "Book1 has not enough copies to sell. Left: 15")

        self.assertEqual(bs.total_sold_books, 0)

    def test_sell_book(self):
        bs = Bookstore(100)
        bs.availability_in_store_by_book_titles = {"Book1": 20, "Book2": 30}

        self.assertEqual(bs.sell_book("Book1", 10), "Sold 10 copies of Book1")
        self.assertEqual(bs.total_sold_books, 10)

        self.assertEqual(bs.sell_book("Book2", 10), "Sold 10 copies of Book2")

        self.assertEqual(bs.total_sold_books, 20)

    def test_str(self):
        bs = Bookstore(100)
        bs.availability_in_store_by_book_titles = {"Book1": 10, "Book2": 10}
        bs.sell_book("Book1", 5)

        expected = "Total sold books: 5\n"
        expected += "Current availability: 15\n"
        expected += " - Book1: 5 copies\n"
        expected += " - Book2: 10 copies"

        self.assertEqual(str(bs), expected)


if __name__ == "__main__":
    main()
