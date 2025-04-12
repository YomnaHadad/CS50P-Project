import random
def main():
    score = generate_integer(get_level())
    print(score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1,4):
                return level
        except:
            pass

def generate_integer(level):
    cnt = 0
    for _ in range(10):
        if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
        else:
            x = random.randint(100,999)
            y = random.randint(100,999)

        print(f"{x} + {y} =" , end=" ")
        try:
            for i in range(3):
                ans = int(input(""))
                if ans == x + y:
                    cnt+=1
                    break
                else:
                    if i == 2:
                        print("EEE")
                        print(f"{x} + {y} =" , x+y )
                    else:
                        print("EEE")
                        print(f"{x} + {y} =" , end=" ")
        except:
            pass
    return cnt

if __name__ == "__main__":
    main()
