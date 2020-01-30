combination = ['S', 'S', 'N', 'W', 'E', 'S']
index = 0
moves = 0
trials = 0
lives = 3
flag = True

while flag :
    userInput = input("You are in the magic maze. Which way (N,S,E,W) do you want to go? ")
    moves += 1
    index += 1
    if index <= (len(combination)-1) :
        if userInput != combination[index-1] :
            index = 0
            trials += 1
            if (trials % 5) == 0 :
                lives -= 1
                if lives >= 1 :
                    print("You have lost one life. You still have", lives, "left.")
                else :
                    flag = False
                    print("Game Over")
                    break
            print("Wrong way. You are back in the start!")
    else :
        flag = False
        print("You have escaped the maze in", moves, "moves")