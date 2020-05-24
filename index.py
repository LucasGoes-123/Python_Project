import uteis
uteis.linhas()
print("Fibonacchi sequence")
uteis.linhas()
n1 = int(input("Type the length of the squence:"))
a = 0
b = 1
s = 0
for c in range(0, n1):
    if c > 1:
        s = a + b
        b = a
        a = s
    print(a, end=", ")
