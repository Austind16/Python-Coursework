import random

def game():
    print("You are playing a game... ")
    score = random.randint(1,100)

    #Fetch the hiscore
    with open("Hi-score.txt") as f:
        hi_score = f.read()
    if (hi_score != ""):
        hi_score = int(hi_score)
    else:
        hi_score = 0

       
    print(f"Your score is {score}")
     #Write the hiscore of the file
    if(score > hi_score):
        #Write the hiscore of the file
        with open("Hi-score.txt", "w") as f:
            f.write(str(score))
    return score

game()