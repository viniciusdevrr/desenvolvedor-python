try:
    number = int(input("Enter a number: "))
    division = 100 / number
    print(f"Division: {division}")
except ZeroDivisionError:
    print("Error: cannot divide by zero")
except ValueError:
    print("Error: cannot divide by that value")
except Exception as error:
    print(f"Unexpected error: {error}")
finally:
    print("End of your code")