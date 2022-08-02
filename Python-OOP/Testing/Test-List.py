class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTest(TestCase):
    def test_init(self):
        integer_list = IntegerList(1, 2, 3, "a")
        self.assertListEqual([1, 2, 3], integer_list._IntegerList__data)

    def test_get_data_method(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertListEqual(integer_list.get_data(), integer_list._IntegerList__data)

    def test_add_method_error(self):
        integer_list = IntegerList(1, 2, 3)

        with self.assertRaises(Exception) as ex:
            integer_list.add("a")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_method_functionality(self):
        integer_list = IntegerList(1, 2, 3)
        integer_list.add(4)
        self.assertListEqual([1, 2, 3, 4], integer_list._IntegerList__data)

    def test_remove_index_method_error(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(Exception) as ex:
            integer_list.remove_index(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_method_functionality(self):
        integer_list = IntegerList(1, 2, 3)
        integer_list.remove_index(1)
        self.assertListEqual([1, 3], integer_list._IntegerList__data)

    def test_get_method_error(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(Exception) as ex:
            integer_list.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_method_functionality(self):
        integer_list = IntegerList(1, 2, 3)
        expected_value = integer_list.get(1)
        self.assertEqual(2, expected_value)

    def test_insert_method_error_1(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(Exception) as ex:
            integer_list.insert(5, 1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method_error_2(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(Exception) as ex:
            integer_list.insert(1, "a")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_method_functionality(self):
        integer_list = IntegerList(1, 2, 3)
        integer_list.insert(1, 1)
        self.assertListEqual([1, 1, 2, 3], integer_list._IntegerList__data)

    def test_get_biggest_method(self):
        integer_list = IntegerList(1, 2, 3)
        expected_value = integer_list.get_biggest()
        self.assertEqual(3, expected_value)

    def test_get_index(self):
        integer_list = IntegerList(1, 2, 3)
        expected_value = integer_list.get_index(1)
        self.assertEqual(0, expected_value)


if __name__ == "__main__":
    main()
