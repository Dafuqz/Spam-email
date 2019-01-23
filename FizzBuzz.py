x = int(input("we will count 4 u!"))
for i in range (1,x+1):
    if i % 56 == 0:
        print ("Fizz Buzz!", i)
    elif i % 7 == 0:
        print("Buzz",i)
    elif i % 8 == 0:
        print ("Fizz", i)
    else:
        print i

