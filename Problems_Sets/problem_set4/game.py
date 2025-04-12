import random
while True:
    try:
        level = int(input("Level: "))
        g = int(input("Guess: "))
        if level <= 100 and type(g) == int:
            secret = random.randrange(level)
    except:
        pass
    else:
        while g >= 0:
            if g > secret:
                print("Too large!")
            elif g < secret:
                print("Too small!")
            else:
                print("Just right!")
                break
            g = int(input("Guess: "))
        break
# python game.py
