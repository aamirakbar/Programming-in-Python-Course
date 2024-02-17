# Lambda function to convert Celsius to Fahrenheit
celsius_to_fahrenheit = lambda celsius: (celsius * 9/5) + 32

# List of Celsius temperatures
celsius_temps = {0, 10, 20, 30, 40}

# Using map to convert Celsius temperatures to Fahrenheit
fahrenheit_temps = map(celsius_to_fahrenheit, celsius_temps)

# Displaying the Fahrenheit temperatures using map
print(list(fahrenheit_temps))  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]
