print ("Hello, enter A:")
A = int(input())
print ("Hello, enter B:")
B = int(input())
print ("Hello, enter C:")
C = int(input())

D=0
X=0

D = (B**2)-(4*A*C)
if (D < 0):
    print ("There are no any roots")
    exit()
if (D == 0):
    X = ((B*(-1))/(2*A))
    print ("There is 1 root:", X)
    exit()
if (D > 0):
    print ("There are 2 roots:")
    X = (((B*(-1))+(D**(0.5)))/(2*A))
    print("X1:", X)
    X = (((B*(-1))-(D**(0.5)))/(2*A))
    print("X2:", X)
    exit()


