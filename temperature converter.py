def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_conversion():
    print("Temperature Conversion Program")

    try:
        temperature = float(input("Enter temperature value: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    print("\nChoose the original unit of measurement:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    try:
        choice = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if choice == 1:
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"\n{celsius} degrees Celsius is equal to:")
        print(f"{fahrenheit:.2f} degrees Fahrenheit")
        print(f"{kelvin:.2f} Kelvin")
    elif choice == 2:
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"\n{fahrenheit} degrees Fahrenheit is equal to:")
        print(f"{celsius:.2f} degrees Celsius")
        print(f"{kelvin:.2f} Kelvin")
    elif choice == 3:
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"\n{kelvin} Kelvin is equal to:")
        print(f"{celsius:.2f} degrees Celsius")
        print(f"{fahrenheit:.2f} degrees Fahrenheit")
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    temperature_conversion()
