from unittest import TestCase, main
from project.train.train import Train


class TestTrain(TestCase):
    def test_class_attributes(self):
        t = Train("Name", 100)
        self.assertEqual(t.TRAIN_FULL, "Train is full")
        self.assertEqual(t.PASSENGER_EXISTS, "Passenger {} Exists")
        self.assertEqual(t.PASSENGER_NOT_FOUND, "Passenger Not Found")
        self.assertEqual(t.PASSENGER_ADD, "Added passenger {}")
        self.assertEqual(t.PASSENGER_REMOVED, "Removed {}")
        self.assertEqual(t.ZERO_CAPACITY, 0)

    def test_init(self):
        t = Train("Name", 100)
        self.assertEqual(t.name, "Name")
        self.assertEqual(t.capacity, 100)
        self.assertEqual(t.passengers, [])

    def test_add_method_train_full_error(self):
        t = Train("Name", 1)
        t.passengers = ["Mitko"]

        with self.assertRaises(Exception) as ex:
            t.add("Gosho")
        self.assertEqual(str(ex.exception), "Train is full")

    def test_add_method_passenger_exists(self):
        t = Train("Name", 2)
        t.passengers = ["Mitko"]

        with self.assertRaises(Exception) as ex:
            t.add("Mitko")
        self.assertEqual(str(ex.exception), "Passenger Mitko Exists")

    def test_add_method_no_error_case(self):
        t = Train("Name", 2)
        t.passengers = ["Mitko"]

        self.assertEqual(t.add("Gosho"), "Added passenger Gosho")
        self.assertListEqual(t.passengers, ["Mitko", "Gosho"])

    def test_remove_method_error(self):
        t = Train("Name", 2)
        t.passengers = ["Mitko"]

        with self.assertRaises(Exception) as ex:
            t.remove("Gosho")
        self.assertEqual(str(ex.exception), "Passenger Not Found")
        self.assertListEqual(t.passengers, ["Mitko"])

    def test_remove_method_no_error_case(self):
        t = Train("Name", 2)
        t.passengers = ["Mitko", "Gosho"]

        self.assertEqual(t.remove("Gosho"), "Removed Gosho")
        self.assertListEqual(t.passengers, ["Mitko"])


if __name__ == "__main__":
    main()
