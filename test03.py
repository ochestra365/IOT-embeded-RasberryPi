#함수

def min(a,b):
    if (a>b):
        return b
    else:
        return a

c=min(10,20)
print (c)

def prints(c):
    print(c)
prints("hello World")

def divide(a,b):
    return (a/b,a%b)
d,v=divide(4,2)
print(d,v)
print(type(d))