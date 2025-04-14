def feet_to_inches(feet):
    inches_per_foot = 12
    return feet * inches_per_foot

while True:
    user_input = input("Enter length in feet (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Exiting program.")
        break

    try:
        feet = float(user_input)
        if feet < 0:
            print("Length cannot be negative. Try again.\n")
            continue
        inches = feet_to_inches(feet)
        foot_label = "foot" if feet == 1 else "feet"
        print(f"{feet} {foot_label} = {inches} inches\n")
    except ValueError:
        print("Invalid input. Please enter a numeric value.\n")
