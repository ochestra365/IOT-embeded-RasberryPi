#변수 기본
n=1
name ='Park'
n=n+2
value=1.2*n

#print('{0} = 1.2*{1}'.format(value,n))
#print(name)

#문자열 배열(방식)
greeting='Hello World'
#print(greeting[0]) #H
#print(greeting[2:7]) #llo
#print(greeting[:2]) #l
#print(greeting[-2:]) #ld
#print(greeting*2)

numbers=[0,1,2,3]
#print(numbers)
#print(numbers[0])
#print(numbers[2:4])
names=['Kim','Lee','Park','Choi']
array = numbers + names
print(array)
print(array[-1])
print(array*2)

#Tuple
person = ('Kim',24,'male')
print(person)
print(person[1])
#person[1]=45
name, age, gender = person
print(gender)