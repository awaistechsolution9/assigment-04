def get_first_element(lst):
    print(lst[0])

# User input
n = int(input("How many elements? "))
lst = [input("Enter element: ") for _ in range(n)]

get_first_element(lst)
