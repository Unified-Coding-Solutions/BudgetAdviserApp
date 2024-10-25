# Description: This file contains the Expenses class which is used to calculate the total expenses for the person


class Expenses:
    def __init__(
        self,
        health_insurance: float,
        phone: float,
        car_insrance: float,
        internet: float,
        gas: float,
        groceries: float,
        rent: float,
        animal_food: float,
        bank_fees: float,
        credit_card_payment: float,
        clothing: float,
        utilities: float,
        debt_payment: float,
        tfsa: float,
        rrsp: float,
        savings: float,
        allowance: float,
    ):
        self.health_insurance = health_insurance
        self.phone = phone
        self.car_insrance = car_insrance
        self.internet = internet
        self.gas = gas
        self.groceries = groceries
        self.rent = rent
        self.animal_food = animal_food
        self.bank_fees = bank_fees
        self.credit_card_payment = credit_card_payment
        self.clothing = clothing
        self.utilities = utilities
        self.debt_payment = debt_payment
        self.tfsa = tfsa
        self.rrsp = rrsp
        self.savings = savings
        self.allowance = allowance

    def total_expenses(self):
        """
        This method calculates the total expenses for the person

        Returns:
            float: The total expenses for the person
        """
        expense_list = [
            self.health_insurance,
            self.phone,
            self.car_insrance,
            self.internet,
            self.gas,
            self.groceries,
            self.rent,
            self.animal_food,
            self.bank_fees,
            self.credit_card_payment,
            self.clothing,
            self.utilities,
            self.debt_payment,
            self.tfsa,
            self.rrsp,
            self.savings,
            self.allowance,
        ]
        total = sum(float(i) for i in expense_list)
        return round(total, 2)
