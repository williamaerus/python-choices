import random
import time 
options = []
def askoptions():					#qui chiede che opzione si vuole aggiungere
    option = input("what option do you want to add?\n")
    options.append(option)
    option = ""
    print ("the options until now are ",options)
    time.sleep(0.5)
    choiceadd()								#qui rimanda alla funzione che chiede se si vogliono aggiungere altre opzioni
def choiceadd():
    quest = input("do you want to add other options?\n")		#qui l'obbiettivo è chiedere se si vuole aggiungere un opzione, se si rimanda ad askoptions se no allora sceglie a caso una delle opzioni e la
    if quest in ["yes" or "YES" or "Yes" or "y" or "Y"]:			#mette a schermo
        askoptions()
    if quest in ["no" or "NO" or "No" or "n" or "N"]:
        answer = random.choice(options)
        print("my answer is...")
        time.sleep(3)
        print(answer)
def start():
    print("first start")
    askoptions()
start()