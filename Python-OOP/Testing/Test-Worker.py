# Code that is going to be tested
class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

# Tests:
from unittest import TestCase, main


class TestWorker(TestCase):
    def test_if_initialized_correctly(self):
        worker = Worker("Kaloyan", 123, 1)

        self.assertEqual("Kaloyan", worker.name)
        self.assertEqual(123, worker.salary)
        self.assertEqual(1, worker.energy)
        self.assertEqual(0, worker.money)

    def test_rest_method(self):
        worker = Worker("Kaloyan", 123, 1)
        worker.rest()
        self.assertEqual(worker.energy, 2)

    def test_energy_0_or_less_after_work_method(self):
        worker = Worker("Kaloyan", 123, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_money_update(self):
        worker = Worker("Kaloyan", 123, 1)
        worker.work()
        self.assertEqual(123, worker.money)

    def test_work_energy_update(self):
        worker = Worker("Kaloyan", 123, 2)
        worker.work()
        self.assertEqual(1, worker.energy)

    def test_get_info(self):
        worker = Worker("Kaloyan", 123, 1)
        self.assertEqual('Kaloyan has saved 0 money.', worker.get_info())


if __name__ == "__main__":
    main()
