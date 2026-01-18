import random
cp = random.randint(1,100)
while True:
    player = input("Guess the number (1-100):")
    numb = int(player)
    if numb != cp:
        if numb > cp:
            print(f"The number {numb} is higher than the number")
        if numb < cp:
            print(f"The number {numb} is lower than the number")
    if player == str(cp):
        print("You Win!")
        break
