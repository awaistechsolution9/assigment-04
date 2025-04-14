def phonebook():
    phonebook_dict = {}
    
    phonebook_dict["Alice"] = "123-456-7890"
    phonebook_dict["Bob"] = "234-567-8901"
    phonebook_dict["Charlie"] = "345-678-9012"
    
    print("Phonebook:")
    for name, number in phonebook_dict.items():
        print(f"{name}: {number}")
    
    name_to_lookup = input("\nEnter a name to look up the phone number: ")
    
    if name_to_lookup in phonebook_dict:
        print(f"The phone number for {name_to_lookup} is: {phonebook_dict[name_to_lookup]}")
    else:
        print(f"{name_to_lookup} is not in the phonebook.")

phonebook()
