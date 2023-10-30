# This is a program that calculates the area and circumference of a circle

# Import the math module to use the pi constant
import math

# Define a function to calculate the area of a circle
def calculate_area(radius):
    # Use the formula for the area of a circle: pi * radius^2
    return math.pi * (radius ** 2)

# Define a function to calculate the circumference of a circle
def calculate_circumference(radius):
    # Use the formula for the circumference of a circle: 2 * pi * radius
    return 2 * math.pi * radius

# Get the radius of the circle from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area and circumference of the circle
area = calculate_area(radius)
circumference = calculate_circumference(radius)

# Print the results
print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")
