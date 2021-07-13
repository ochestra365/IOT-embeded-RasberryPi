#import Mapping
m=0
n=1

def func():
    global m#전역변수를 사용하겠다
    global n#전역변수를 사용하겠다.
    m= m + 1
    n+=1
func()
print(m,n)

def counter(max):
    t=0

    def output():#counter 함수에 속하는 함수, 따로 호출이 불가능하다.
        print('t={0}'.format(t))

    while t<max:
        output()
        t+=1

counter(10)

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(9))
#lamda
a= lambda x,y:x*y
print(a(2,8))

#Closure

def calc(a):
    def add(b):
        return a+b
    return add



sum=calc(1)
print(sum(2))


