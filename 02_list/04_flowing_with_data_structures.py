def add_three_copies(lst, data):
    for _ in range(3):
        lst.append(data)

# User input
msg = input("Enter a message to copy: ")

my_list = []
print("List before:", my_list)

add_three_copies(my_list, msg)

print("List after:", my_list)
