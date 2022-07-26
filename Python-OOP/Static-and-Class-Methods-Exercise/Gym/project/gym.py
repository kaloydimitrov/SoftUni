from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def __adds_object_to_list(self, obj, current_list: list):
        if obj not in current_list:
            current_list.append(obj)
        return current_list

    def add_customer(self, customer: Customer):
        self.customers = self.__adds_object_to_list(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.trainers = self.__adds_object_to_list(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.equipment = self.__adds_object_to_list(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.plans = self.__adds_object_to_list(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.subscriptions = self.__adds_object_to_list(subscription, self.subscriptions)

    def __finds_obj_by_id(self, id, current_list: list):
        for obj in current_list:
            if obj.id == id:
                return obj

    def subscription_info(self, subscription_id: int):
        subscription: Subscription = self.__finds_obj_by_id(subscription_id, self.subscriptions)
        customer = self.__finds_obj_by_id(subscription.customer_id, self.customers)
        trainer = self.__finds_obj_by_id(subscription.trainer_id, self.trainers)
        plan: ExercisePlan = self.__finds_obj_by_id(subscription.exercise_id, self.plans)
        equipment = self.__finds_obj_by_id(plan.equipment_id, self.equipment)

        result = repr(subscription) + "\n"
        result += repr(customer) + "\n"
        result += repr(trainer) + "\n"
        result += repr(equipment) + "\n"
        result += repr(plan)

        return result
