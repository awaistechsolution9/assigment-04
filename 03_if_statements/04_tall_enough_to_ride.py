def check_height():
    MIN_HEIGHT = 50  

    while True:
        height = input("How tall are you? ")

        if height == "":
            break  

        height = int(height)  

        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

check_height()
