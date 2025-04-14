def count_even(lst):

    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break  
        else:
            lst.append(int(user_input)) 
    
    even_count = 0
    for number in lst:
        if number % 2 == 0:
            even_count += 1
    
    print(f"Number of even numbers: {even_count}")
    
numbers_list = []
count_even(numbers_list)
