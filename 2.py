print("Hello, enter 2 words:")

a = input()
b = input()

a_temp = list(a)
b_temp = list(b)

a_temp.sort()
b_temp.sort()


if a_temp == b_temp:
    print(a, "and", b, "are anagramas")
else:
    print(a, "and", b, "are not anagramas")



