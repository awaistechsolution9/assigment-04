def count_numbers(lst):

    count_dict = {}
    
    for number in lst:
        if number in count_dict:

            count_dict[number] += 1
        else:
            count_dict[number] = 1
    
    for number, count in count_dict.items():
        print(f"{number}: {count}")

numbers = [1, 2, 3, 2, 4, 1, 2, 3, 3, 3, 4]

count_numbers(numbers)
