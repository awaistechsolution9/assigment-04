MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        print(f"Removed: {lst.pop()}")

# Main function to test
def main():
    lst = input("Enter a list of values (separate with spaces): ").split()
    shorten(lst)

main()
