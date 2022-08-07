from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def test_init(self):
        p = Plantation(4)
        self.assertEqual(p.size, 4)
        self.assertEqual(p.plants, {})
        self.assertEqual(p.workers, [])

    def test_size_error(self):
        with self.assertRaises(Exception) as ex:
            p = Plantation(-1)
        self.assertEqual(str(ex.exception), "Size must be positive number!")

    def test_hire_worker(self):
        p = Plantation(4)

        self.assertEqual(p.hire_worker("Petkan"), "Petkan successfully hired.")

    def test_hire_worker_error(self):
        p = Plantation(4)
        p.hire_worker("Petkan")
        with self.assertRaises(Exception) as ex:
            p.hire_worker("Petkan")
        self.assertEqual(str(ex.exception), "Worker already hired!")

    def test_len(self):
        p = Plantation(4)
        p.plants = {"neshto": [4, 6], "drugo": [6, 4, 4]}
        self.assertEqual(len(p), 5)

    def test_planting_worker_not_hired_error(self):
        p = Plantation(4)
        with self.assertRaises(Exception) as ex:
            p.planting("Petkan", "Marulq")
        self.assertEqual(str(ex.exception), "Worker with name Petkan is not hired!")

    def test_planting_is_full(self):
        p = Plantation(4)
        p.hire_worker("Petkan")
        p.plants = {"neshto": [4, 6], "drugo": [6, 4, 4]}
        with self.assertRaises(Exception) as ex:
            p.planting("Petkan", "Marulq")
        self.assertEqual(str(ex.exception), "The plantation is full!")

    def test_planting1(self):
        p = Plantation(4)
        p.hire_worker("Petkan")
        p.plants = {"Petkan": ["Gluhar4e"]}

        self.assertEqual(p.planting("Petkan", "Marulq"), "Petkan planted Marulq.")
        self.assertDictEqual(p.plants, {"Petkan": ["Gluhar4e", "Marulq"]})

    def test_planting2(self):
        p = Plantation(4)
        p.hire_worker("Petkan")

        self.assertEqual(p.planting("Petkan", "Marulq"), "Petkan planted it's first Marulq.")
        self.assertDictEqual(p.plants, {"Petkan": ["Marulq"]})

    def test_str(self):
        p = Plantation(4)
        p.hire_worker("Petkan")
        p.hire_worker("Mitko")
        p.plants = {"Petkan": ["Gluhar4e"]}

        self.assertEqual(str(p), "Plantation size: 4\nPetkan, Mitko\nPetkan planted: Gluhar4e")

    def test_repr(self):
        p = Plantation(4)
        p.hire_worker("Petkan")
        p.hire_worker("Mitko")

        self.assertEqual(repr(p), "Size: 4\nWorkers: Petkan, Mitko")


if __name__ == "__main__":
    main()
