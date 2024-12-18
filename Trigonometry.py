import math

def calculate_trigonometric_values(angle_degrees):
    
    angle_radians = math.radians(angle_degrees)

    sine_value = math.sin(angle_radians)
    cosine_value = math.cos(angle_radians)
    tangent_value = math.tan(angle_radians)

    return sine_value, cosine_value, tangent_value

try:
    angle = float(input("Enter the angle in degrees: "))
    sine, cosine, tangent = calculate_trigonometric_values(angle)

    print(f"Sine({angle}) = {sine}")
    print(f"Cosine({angle}) = {cosine}")
    print(f"Tangent({angle}) = {tangent}")

except ValueError:
    print("Invalid input! Please enter a numeric value for the angle.")