# Description: This file contains utility functions that are used throughout the application
from typing import Optional
import time
import typer
from rich.progress import track
from Coding.BudgetAdviserApp.expenses import Expenses
from Coding.BudgetAdviserApp.person import Person


def user_login(username: str, password: str) -> bool:
    """
    This function checks if the user's login credentials are correct

    args:
        username (str): The user's username
        password (str): The user's password

    Returns:
        bool: True if the login credentials are correct, False otherwise
    """
    if username == "admin" and password == "admin":
        return True
    return False


def progress_bar(description) -> None:
    """
    This function creates a progress bar that tracks the progress of a task

    Args:
        description (str): The description of the task being tracked

    Returns:
        None
    """
    total = 0
    for value in track(range(100), description=description):
        time.sleep(0.01)
        total += 1


def welcome_message() -> None:
    """
    This function displays a welcome message to the user

    Returns:
        None
    """
    typer.secho("\nWelcome to the Budget Advisor App", fg=typer.colors.GREEN)


def create_person(
    name: str,
    age: int,
    martial_status: str,
    children: int,
    monthly_income: int,
    monthly_expenses: Expenses,
) -> Person:
    """
    This function creates a Person object

    Args:
        name (str): The name of the person
        age (int): The age of the person
        martial_status (str): The martial status of the person
        children (int): The number of children the person has
        monthly_income (int): The monthly income of the person
        monthly_expenses (Expenses): The monthly expenses of the person

    Returns:
        Person: A Person object
    """
    return Person(name, age, martial_status, children, monthly_income, monthly_expenses)


def create_expenses(
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
) -> Expenses:
    """
    This function creates an Expenses object

    Args:
        health_insurance (float): The amount spent on health insurance
        phone (float): The amount spent on phone bills
        car_insrance (float): The amount spent on car insurance
        internet (float): The amount spent on internet
        gas (float): The amount spent on gas
        groceries (float): The amount spent on groceries
        rent (float): The amount spent on rent
        animal_food (float): The amount spent on animal food
        bank_fees (float): The amount spent on bank fees
        credit_card_payment (float): The amount spent on credit card payments
        clothing (float): The amount spent on clothing
        utilities (float): The amount spent on utilities
        debt_payment (float): The amount spent on debt payments
        tfsa (float): The amount spent on TFSA
        rrsp (float): The amount spent on RRSP
        savings (float): The amount spent on savings
        allowance (float): The amount spent on allowance

    Returns:
        Expenses: An Expenses object
    """
    return Expenses(
        health_insurance,
        phone,
        car_insrance,
        internet,
        gas,
        groceries,
        rent,
        animal_food,
        bank_fees,
        credit_card_payment,
        clothing,
        utilities,
        debt_payment,
        tfsa,
        rrsp,
        savings,
        allowance,
    )


def get_expenses() -> Expenses:
    """
    This function gets the user's monthly expenses

    Returns:
        Expenses: An Expenses object
    """
    health_insurance = typer.prompt("Health Insurance")
    phone = typer.prompt("Phone")
    car_insrance = typer.prompt("Car Insurance")
    internet = typer.prompt("Internet")
    gas = typer.prompt("Gas")
    groceries = typer.prompt("Groceries")
    rent = typer.prompt("Rent")
    animal_food = typer.prompt("Animal Food")
    bank_fees = typer.prompt("Bank Fees")
    credit_card_payment = typer.prompt("Credit Card Payment")
    clothing = typer.prompt("Clothing")
    utilities = typer.prompt("Utilities")
    debt_payment = typer.prompt("Debt Payment")
    tfsa = typer.prompt("TFSA")
    rrsp = typer.prompt("RRSP")
    savings = typer.prompt("Savings")
    allowance = typer.prompt("Allowance")
    return create_expenses(
        health_insurance,
        phone,
        car_insrance,
        internet,
        gas,
        groceries,
        rent,
        animal_food,
        bank_fees,
        credit_card_payment,
        clothing,
        utilities,
        debt_payment,
        tfsa,
        rrsp,
        savings,
        allowance,
    )


def get_person() -> Person:
    """
    This function gets the user's information

    Returns:
        Person: A Person object
    """
    name = typer.prompt("Name")
    age = typer.prompt("Age")
    martial_status = typer.prompt("Martial Status (M/S)")
    children = typer.prompt("Number of Children")
    monthly_income = typer.prompt("Monthly Income")
    monthly_expenses = get_expenses()
    return create_person(
        name, age, martial_status, children, monthly_income, monthly_expenses
    )


def cal_total_expenses(expenses: Expenses) -> float:
    """
    This function calculates the total monthly expenses

    Args:
        expenses (Expenses): The monthly expenses

    Returns:
        float: The total monthly expenses
    """
    return float(expenses.total_expenses())


def cal_total_income(person: Person) -> float:
    """
    This function calculates the total monthly income

    Args:
        person (Person): The person object

    Returns:
        float: The total monthly income
    """
    return float(person.monthly_income)


def cal_budget(person: Person) -> float:
    """
    This function calculates the budget

    Args:
        person (Person): The person object

    Returns:
        float: The budget
    """
    return cal_total_income(person) - cal_total_expenses(person.monthly_expenses)


def login() -> str:
    """
    This function logs the user in

    Returns:
        str: The username of the user
    """
    username = typer.prompt("Username")
    password = typer.prompt("Password", hide_input=True)
    total = 0
    while total < 1:
        progress_bar("Logging in...")
        total += 1
    if user_login(username, password):
        typer.secho("Login Successful", fg=typer.colors.GREEN)
        return username
    else:
        typer.secho("Login Failed", fg=typer.colors.RED)
        raise typer.Abort()


def display_budget_breakdown(person: Person) -> None:
    """
    This function displays the budget breakdown

    Args:
        person (Person): The person object

    Returns:
        None
    """
    budget = cal_budget(person)
    typer.secho(
        f"Monthly Income: {
                cal_total_income(person)}",
        fg=typer.colors.GREEN,
    )
    typer.secho(
        f"Monthly Expenses: {cal_total_expenses(
        person.monthly_expenses)}",
        fg=typer.colors.RED,
    )
    progress_bar(f"Calculating budget breakdown for {person.name}...")
    typer.secho("\nBudget breakdown:", fg=typer.colors.GREEN)
    typer.echo(f"Health Insurance: {person.monthly_expenses.health_insurance}")
    typer.echo(f"Phone: {person.monthly_expenses.phone}")
    typer.echo(f"Car Insurance: {person.monthly_expenses.car_insrance}")
    typer.echo(f"Internet: {person.monthly_expenses.internet}")
    typer.echo(f"Gas: {person.monthly_expenses.gas}")
    typer.echo(f"Groceries: {person.monthly_expenses.groceries}")
    typer.echo(f"Rent: {person.monthly_expenses.rent}")
    typer.echo(f"Animal Food: {person.monthly_expenses.animal_food}")
    typer.echo(f"Bank Fees: {person.monthly_expenses.bank_fees}")
    typer.echo(
        f"Credit Card Payment: {
               person.monthly_expenses.credit_card_payment}"
    )
    typer.echo(f"Clothing: {person.monthly_expenses.clothing}")
    typer.echo(f"Utilities: {person.monthly_expenses.utilities}")
    typer.echo(f"Debt Payment: {person.monthly_expenses.debt_payment}")
    typer.echo(f"TFSA: {person.monthly_expenses.tfsa}")
    typer.echo(f"RRSP: {person.monthly_expenses.rrsp}")
    typer.echo(f"Savings: {person.monthly_expenses.savings}")
    typer.echo(f"Allowance: {person.monthly_expenses.allowance}")


def is_within_budget(
    person: Person,
    spouse: Optional[Person],
) -> bool:
    """
    This function checks if the user is within budget

    Args:
        person (Person): The person object
        spouse (Optional[Person]): The spouse object

    Returns:
        bool: True if the user is within budget, False otherwise
    """
    if spouse is None:
        monthly_income = int(person.monthly_income)
        monthly_expenses = cal_total_expenses(person.monthly_expenses)
    else:
        monthly_income = int(person.monthly_income) + int(spouse.monthly_income)
        monthly_expenses = cal_total_expenses(
            person.monthly_expenses
        ) + cal_total_expenses(spouse.monthly_expenses)
    if int(person.children) > 0:
        child_expenses = typer.prompt("Monthly Child Expenses")
        monthly_expenses = int(monthly_expenses)
        monthly_expenses += int(child_expenses) * int(person.children)
    budget = int(monthly_income) - int(monthly_expenses)
    if budget > 0:
        typer.secho(f"\n\nExpenses: {monthly_expenses}", fg=typer.colors.RED)
        typer.secho(f"Budget: {budget}", fg=typer.colors.GREEN)
        typer.secho("You are within budget", fg=typer.colors.GREEN)
        return True
    else:
        typer.secho(f"\n\nExpenses: {monthly_expenses}", fg=typer.colors.RED)
        typer.secho(f"Budget: {budget}", fg=typer.colors.RED)
        typer.secho("You are over budget", fg=typer.colors.RED)
        return False
