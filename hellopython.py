n = input("Enter an integer between 1 to 100")
if(int(n)%2 != 0):
    print("Weird")
else :
    if (int(n) >= 2 and int(n) <= 5 ):
        print("Not Weird")
    elif (int(n) >= 6 and int(n) <= 20 ):
        print("Weird")
    else:
        print("Not Weird")



