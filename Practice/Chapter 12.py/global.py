a = 89

def func():
    global a
    a =3
    print(a)

func()
print(a)

def func():
    #global a
    a =56
    print(a)

func()
print(a)