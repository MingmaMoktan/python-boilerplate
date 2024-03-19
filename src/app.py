'''
Contains the application logic.
'''

from src.user.user import User
from src.user.group import Group

def main() -> None: # pragma: no cover
    '''
    Runs the main logic of the application.
    '''
    print("Hello!")

    user = User(1, "Aleksi")
    print(user)

    group_admins = Group(1, "Admins")
    group_admins.add_user(user)
    print(group_admins)

def sum(num1 : int, num2 : int) -> int:
    '''
    Takes in two numbers and returns the result of the sum operation of the given two numbers.

    Args:
        num1 (int): First number
        num2 (int): Second number
    
    Returns:
        int: The result of the sum operation.

    Raises:
        TypeError: If one of the passed arguments is not numeric, then this is raised.
    '''
    return num1 + num2