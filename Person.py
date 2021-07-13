class Person(object):
    total =0

    def __init__(self,name,age):#기본 생성자(self) / 오버로딩 생성자
        self.name = name
        self.age=age
    def getAge(self):
        return self.age

class Man(Person):#Man은 Person을 상속받는다.
    gender='male'
#포인터가 된다. C#이랑 자바는 다중상속이 안된다. 인터페이스문제도 생김.
class Korean(Person):
    nationlity='Korea'

class KoreanMan(Man,Korean):
    pass#나중에 개발하겠다. 확장성을 위한 것이다. 상속 문제는 개인에 따른 것이다.