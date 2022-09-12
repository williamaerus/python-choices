import random
choices = ["do","don't do"]
def makedecision():
    name = input("what do you want me to choose for?            \n")
    solution = random.choice(choices)
    print(solution)
makedecision()
