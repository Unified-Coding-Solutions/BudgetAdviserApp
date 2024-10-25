# Description: This is the main file for the Budget Advisor application. It contains the main logic for the application.

# Importing the necessary libraries
import typer
from utils import (
    login,
    welcome_message,
    get_person,
    display_budget_breakdown,
    is_within_budget,
)

# Creating a Typer app instance
app = typer.Typer(name="Budget Advisor")


# Defining the main command for the Typer app
@app.command()
def budget() -> None:
    """
    This command is used to run the Budget Advisor application

    How It Works:
    - Logs the user in
    - Displays a welcome message
    - Gets the user's information
    - Displays the budget breakdown
    - Checks if the user is within budget

    Returns:
        None
    """
    # Logging the user in and displaying a welcome message
    login()
    welcome_message()
    person = get_person()

    # Displaying the budget breakdown
    # If the person is married, we get the information for the second person
    # and display the budget breakdown for both persons
    # We then check if the total budget is within the budget
    # If the person is single, we display the budget breakdown for the person
    # and check if the total budget is within the budget
    # The results are displayed in the terminal
    if person.martial_status == "M":
        person2 = get_person()
        typer.echo("Person 1:")
        display_budget_breakdown(person)
        typer.echo("\n\n")
        typer.echo("Person 2:")
        display_budget_breakdown(person2)
        is_within_budget(person, person2)
    else:
        typer.echo("\n\n")
        display_budget_breakdown(person)
        is_within_budget(person, None)


# Running the Typer app
if __name__ == "__main__":
    app()
