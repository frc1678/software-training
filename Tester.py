# Fun test program
testA = "3|(y + |(y^2 + z^3)) + 3|(y - |(y^2 + z^3)) - b/3a"
testB = "c/3a - b^2/9a^2"
testC = "-b^3/37a^3 + bc/6a^2 - d/2a"
answerA = input("x =    ")
if(answerA == testA or answerA == "skip"):
    answerB = input("z =    ")
    if(answerB == testB or answerB == "skip"):
        answerC = input("y =    ")
        if(answerC== testC or answerC == "skip"):
            answerC = input("Congrats! All questions are correct")
        else:
            print("x ACTUALLY = " + testC)
    else:
        print("x ACTUALLY = " + testB)
else:
    print("x ACTUALLY = " + testA)
