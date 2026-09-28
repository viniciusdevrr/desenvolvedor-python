while True:
    value = ""
    try:
        value = int(input("Enter password: "))
    except Exception as erro:
        print(f"Unexpected error: {erro}")
    finally:
        if value == 1234:
            break