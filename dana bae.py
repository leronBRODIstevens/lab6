#25

x = 1
while (x < 300) :
    print x
    x = x + 2
    
#25

myCocaineList = [5,67,98,23,75,"swag",873,96,"what happened to ronald regan"]
index = 0
while (index<len(myCocaineList)) :
    print myCocaineList[index]
    index = index + 1
    
#50
import random
rand = random.randint(0,50)
print "Guess a number"
userInput = -1
while (userInput != rand):
    userInput = int(raw_input())
    if (userInput < rand):
        print "too low"
    if (userInput > rand):
        print "too high"
    if (userInput == rand):
        print "congratulations!"