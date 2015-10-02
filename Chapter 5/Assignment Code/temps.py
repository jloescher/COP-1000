# Jonathan Loescher SPC ID: 2307132

# Celsius to Fahrenheit: T°F = (T°C × 1.8) + 32
# Fahrenheit to Celsius: T°C = 0.5556 * (T°F - 32)

# Psuedocode
# Define function fahr_to_celsius and set parameter to fahr.
# Define variable cel within fahr_to_celsius function, then use fahr parameter along with Fahrenheit to Celsius equation. Then assign product of equation to the cel variable.
# Return the value of cel.
# Define function celsius_to_fahr and set parameter to cel.
# Define variable fahr within celsius_to_fahr function, then use cel parameter along with the Celsius to Fahrenheit equation, Then assign product of equation to the cel variable.

def fahr_to_celsius(fahr):
    cel = 0.5556 * (fahr - 32)  # Assign product of equation to cel.
    return cel  # Return to variable that executed the function.

def celsius_to_fahr(cel):
    fahr = (cel * 1.8) + 32  # Assign product of equation to fahr.
    return fahr  # Return to variable that executed the function.

# Collaboration Statement: I worked alone.
