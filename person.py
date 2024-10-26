# Description: This file contains the Person class which is used to store the information of a person.

from expenses import Expenses


class Person:
    def __init__(
        self,
        name: str,
        age: int,
        martial_status: str,
        children: int,
        monthly_income: int,
        monthly_expenses: Expenses,
    ):
        self.name = name
        self.age = age
        self.martial_status = martial_status
        self.children = children
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses
