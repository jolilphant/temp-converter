Objective:
In this assignment, you will create a program that converts temperatures between Celsius and Fahrenheit. You'll practice writing functions in Python and handling user input, with a specific format for the final output.

Instructions:
User Input:

Ask the user whether they are providing a Fahrenheit (F) temperature to convert to Celsius (C), or a Celsius (C) temperature to convert to Fahrenheit (F).
Functions:

Write two separate functions:
fahrenheit_to_celsius(fahrenheit): This function should take a temperature in Fahrenheit as an argument and return the temperature converted to Celsius.
celsius_to_fahrenheit(celsius): This function should take a temperature in Celsius as an argument and return the temperature converted to Fahrenheit.
Both functions should have no side effects (i.e., they should only return the value, not print anything).
Program Logic:

Based on the user’s input, call the appropriate function.

After getting the result from the function, print the converted temperature in the following format:

Converted Temperature: {temp_value}
The {temp_value} should be the calculated temperature, formatted as a floating-point number with one decimal place.

## Formulae

- **Fahrenheit → Celsius:**  
  $C = \tfrac{5}{9}(F - 32)$

- **Celsius → Fahrenheit:**  
  $F = \tfrac{9}{5}C + 32$

Example Interaction:
Are you converting from (C)elsius or (F)ahrenheit? F Enter the Fahrenheit temperature: 68 Converted Temperature: 20.0
Deliverable:
Submit your completed program on GitHub, ensuring that:

You include two functions: fahrenheit_to_celsius() and celsius_to_fahrenheit().
The final output is printed in the format Converted Temperature: {temp_value} to work with the auto-grader.
