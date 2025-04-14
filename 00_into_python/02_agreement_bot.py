# 02_agreement_bot

question = input("What is your favourite animal?")

# Answer in bold
bold_animals = f"\033[1m{question}\033[0m"

# User Answer
print(f"My favourite animal is {bold_animals}!")