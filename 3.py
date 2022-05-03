def IsIdeal (num):

    num_del = 0;

    for i in range (1, number):
        if ((num % i) == 0):
            num_del += i

    if num == num_del:
        return(True)
    else:
        return(False)

print("Hello, enter a number")
number = int(input())


if IsIdeal (number) == True:
    print ("Entered number:", number, "is ideal")
else:
    print ("Entered number:", number, ", is not ideal")


