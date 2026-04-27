numeric = int(input("Enter a number less than 25\n"))
if numeric > 25 :
    print("Error")
while numeric <= 25 :
    print(f"Inside the loop, my variable is {numeric}")
    numeric += 1