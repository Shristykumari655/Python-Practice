def celsius_to_fahrenheit(celsius):
    return (celsius*9/5) +32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9
print("Temperature converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2):"))
if choice==1:
    celsius = float(input("Enter temperature in Celsius:"))
    result = celsius_to_fahrenheit(celsius)
    print("Temperature in Fahrenheit:", result)

elif choice==2:
    fahrenheit= float(input("Enter temperature in Fahrenheit:"))
    result = fahrenheit_to_celsius(fahrenheit)
    print("Temperature in Celsius:", result)

else:
    print("Invalid choice!")