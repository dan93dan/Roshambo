import random

def ppt():
    random_dado = random.randint(0, len(options) - 1)
    print(options[random_dado])

options = ['piedra ✊','papel ✋','tijera ✌️']

ppt()

