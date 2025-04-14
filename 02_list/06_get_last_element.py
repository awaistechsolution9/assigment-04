def get_last_element(lst):
    print(lst[-1])

# User input
n = int(input("How many elements? "))
lst = [input("Enter element: ") for _ in range(n)]

get_last_element(lst)
