def celsius_to_fahrenheit(celsius):
    """
    convert celsius to farenheit
    """
    fahrenheit = celsius *1.8 +32
    fahrenheit = round(fahrenheit, 2)
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """
    convert farenheit to celsius
    """
    celsius = (fahrenheit -32) /1.8
    celsius = round(celsius, 2)
    return celsius

print(celsius_to_fahrenheit(15))
print(celsius_to_fahrenheit(25))
print(celsius_to_fahrenheit(38))
print(fahrenheit_to_celsius(100))
print(fahrenheit_to_celsius(115))
print(fahrenheit_to_celsius(75))