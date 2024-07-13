FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

temperature = float(input("Enter the temperature: "))
unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "C":
    converted_temperature = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is equivalent to {converted_temperature}°F")

elif unit == "F":
    converted_temperature = convert_to_celsius(temperature)
    print(f"{temperature}°F is equivalent to {converted_temperature}°C")

else:
    print("Invalid unit. Please enter either C or F.")
