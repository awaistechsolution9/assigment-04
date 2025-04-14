def mass_to_energy(mass):
    c = 3e8
    return mass * c ** 2

while True:
    user_input = input("Enter mass in kilograms (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Exiting program.")
        break

    try:
        mass = float(user_input)
        if mass < 0:
            print("Mass cannot be negative. Try again.")
            continue
        energy = mass_to_energy(mass)
        print(f"Equivalent energy: {energy:.2e} joules\n")
    except ValueError:
        print("Invalid input. Please enter a numeric value.\n")
