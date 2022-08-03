from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def test_init(self):
        vehicle = Vehicle(1, 200)
        self.assertEqual(vehicle.fuel, 1)
        self.assertEqual(vehicle.fuel, vehicle.capacity)
        self.assertEqual(vehicle.fuel_consumption, vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_error(self):
        vehicle = Vehicle(1, 200)
        with self.assertRaises(Exception) as ex:
            vehicle.drive(200)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_method_fuel_decrease(self):
        vehicle = Vehicle(1, 200)
        vehicle.drive(0)
        self.assertEqual(1, vehicle.fuel)

    def test_refuel_error(self):
        vehicle = Vehicle(1, 200)
        with self.assertRaises(Exception) as ex:
            vehicle.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_increases(self):
        vehicle = Vehicle(1, 200)
        vehicle.refuel(0)
        self.assertEqual(1, vehicle.fuel)

    def test_str(self):
        vehicle = Vehicle(1, 200)
        self.assertEqual("The vehicle has 200 horse power with 1 fuel left and 1.25 fuel consumption", str(vehicle))


if __name__ == "__main__":
    main()
