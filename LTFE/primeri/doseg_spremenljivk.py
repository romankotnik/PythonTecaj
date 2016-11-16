a = 0  # a je globalen

if a == 0:
    b = 1  # b je globalen


def fun1(c):
    d = 3  # lokalna spremenljivka
    print(c)  # lokalna spremenljivka
    print(d)


fun1(7)

print(a)
print(b)
#print(c)  # Variable Error; Not defined
#print(d)  # Variable Error; Not defined


for i in [1,2,3,4]:
    print(i)

print(i)

a = 0

def fun2():
    print(a)

print(a)

def fun3():
    #print(a)  # Napaka: uporabljamo lokalni a, preden obstaja
    a = 512
    print(a)

fun2()
print(a)
