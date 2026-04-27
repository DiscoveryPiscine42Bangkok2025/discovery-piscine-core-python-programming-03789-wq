condition = True
while True:
    if condition == True :
        question = input("What you gotta say? : ")
        condition = False
    if question == "STOP" :
        break
    answer = input("I got that! Anything else? : ")
    if answer == "STOP" :
        break