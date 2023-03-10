'''
문제
개의 속성과 행위를 정의하는 Doggy 클래스를 만들어라. 

구성 요소
i.   초기화 메서드는 인자로 개의 이름과 견종을 받아서 인스턴스 변수에 할당한다.
ii.  bark() 메서드를 호출하면 개는 짖을 수 있다.
iii. 클래스 변수는 태어난 개의 숫자와 현재 있는 개의 숫자를 기록하는 변수로 구성한다.
        개가 태어나면 num_of_dogs와 birth_of_dogs의 값이 각 1씩 증가한다.
        개가 죽으면 num_of_dogs의 값이 1 감소한다.
iv.  get_status() 메서드를 호출하면 birth_of_dogs와 num_of_dogs의 수를 출력할 수 있다 
'''

class Doggy:
    num_of_dogs = 0 
    birth_of_dogs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1


    def __del__(self):
        Doggy.num_of_dogs -= 1

    def bark(self):
        print(self.name , '멍멍')

    @classmethod
    def get_status(cls):
        print(f'태어난 강아지 수:{cls.birth_of_dogs}, 강아지 수:{cls.num_of_dogs}')

dog1 = Doggy('흰둥이', '푸들')
dog2 = Doggy('검둥이', '말티즈')
Doggy.bark(dog1)
Doggy.bark(dog2)
Doggy.get_status()
del dog1
Doggy.get_status()
del dog2
Doggy.get_status()


    
