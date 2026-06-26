"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


PREPARATION_TIME = 0
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    
    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time 

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.
    
    Parameters:
        number of layers (int): number of layers added to lasagna.

    Returns:
        int: time taken to prepare the lasagna.

    Funtion returns how much time it will take to prepare the lasagna by taking number_of_layer as argument and multiplying it with 2.
    """
    return number_of_layers * 2
    
#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.

    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    """
    return elapsed_bake_time + (2 * number_of_layers)
    


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
