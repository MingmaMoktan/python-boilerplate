import random

def add(num1 : int, num2 : int) -> int:
    '''
    Adds the two numbers together.

    Args:
        (int): Number 1
        (int): Number 2

    Returns:
        (int): The sum operation of the two passed numbers.
    
    Example:
        >>> add(1, 5)
        6
    '''
    if type(num1)==str or type(num2)==str:
        raise TypeError()
    return num1 + num2

def random_number(min : int, max : int):
    """
    Generates a random number within a specified range.

    This function returns a random integer between the specified minimum and maximum values.

    Args:
        min (int): The minimum value of the range. 
        max (int): The maximum value of the range. 

    Returns:
        int: A random integer within the specified range.

    Example:
        >>> random_number(1, 5)
        3  # This is a possible output; actual output will vary.
    """
    #max = max + 1
    #if min == 5: min = min + 1
    return random.randint(min, max)
