ADULT_AGE = 18

def is_adult(age):
    if age >= ADULT_AGE:
        return True
    else:
        return False

age_input = int(input("How old is this person?: "))
print(is_adult(age_input))
