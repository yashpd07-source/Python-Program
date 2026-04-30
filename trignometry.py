import math

# Ask the user for input (in degrees)
angle_degrees = float(input("Enter an angle in degrees: "))

# Convert degrees to radians
angle_radians = math.radians(angle_degrees)

# Calculate trigonometric values
sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = math.tan(angle_radians)

# Display the results
print(f"sin({angle_degrees}) = {sin_value}")
print(f"cos({angle_degrees}) = {cos_value}")
print(f"tan({angle_degrees}) = {tan_value}")