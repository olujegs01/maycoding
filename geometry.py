# geometry.py

def square_footage(length, width):
    """
    Calculate the square footage of a house.
    
    Args:
    length (float): The length of the house.
    width (float): The width of the house.
    
    Returns:
    float: The area of the house.
    """
    return length * width

def circumference(radius):
    """
    Calculate the circumference of a circle.
    
    Args:
    radius (float): The radius of the circle.
    
    Returns:
    float: The circumference of the circle.
    """
    import math
    return 2 * math.pi * radius
