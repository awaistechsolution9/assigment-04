def collect_values():
    values = []
    while True:
        value = input("Enter a value (press Enter to finish): ")
        if value == "":
            break
        values.append(value)
    print("List of values:", values)

collect_values()
