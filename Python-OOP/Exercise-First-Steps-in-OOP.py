class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


# ---------------------------------------------------------------------------

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, amount):
        self.health += amount

# ---------------------------------------------------------------------------


class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        self.salary *= 12
        return self.salary

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary

# ---------------------------------------------------------------------------


class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        if self.size - self.quantity > quantity:
            self.quantity += quantity

    def status(self):
        return self.size - self.quantity

# ---------------------------------------------------------------------------


