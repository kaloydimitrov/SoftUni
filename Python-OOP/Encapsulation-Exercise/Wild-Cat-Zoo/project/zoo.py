from project.caretaker import Caretaker
from project.keeper import Keeper
from project.cheetah import Cheetah
from project.lion import Lion
from project.animal import Animal
from project.worker import Worker
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.__name} the {animal.__class__.__name__} added to the zoo"

        elif len(self.animals) < self.__animal_capacity:
            return "Not enough budget"

        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.__name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.__name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care_money = 0
        for animal in self.animals:
            total_care_money += animal.money_for_care
        if self.__budget >= total_care_money:
            self.__budget -= total_care_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ""
        lions = [repr(a) + "\n" for a in self.animals if isinstance(a, Lion)]
        tigers = [repr(a) + "\n" for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [repr(a) + "\n" for a in self.animals if isinstance(a, Cheetah)]

        result += f"You have {len(self.animals)} animals\n"

        result += f"----- {len(lions)} Lions:\n"
        result += "".join(lions)

        result += f"----- {len(tigers)} Tigers:\n"
        result += "".join(tigers)

        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += "".join(cheetahs)

        return result.strip()

    def workers_status(self):
        result = ""
        keepers = [repr(a) + "\n" for a in self.workers if isinstance(a, Keeper)]
        caretakers = [repr(a) + "\n" for a in self.workers if isinstance(a, Caretaker)]
        vets = [repr(a) + "\n" for a in self.workers if isinstance(a, Vet)]

        result += f"You have {len(self.workers)} workers\n"

        result += f"----- {len(keepers)} Keepers:\n"
        result += "".join(keepers)

        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "".join(caretakers)

        result += f"----- {len(vets)} Vets:\n"
        result += "".join(vets)

        return result.strip()
