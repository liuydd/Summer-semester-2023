class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 0
        self.smart = 0
        self.health = 0
        
    def play(self):
        self.happiness += 10
        self.smart += 2
        self.health += 6
    
    def eat(self):
        self.happiness += 5
        self.smart += 1
        self.health += 10
        
    def sleep(self):
        self.happiness += 3
        self.smart += 1
        self.health += 5

class Person(Pet):
    def __init__(self, name, money, num):
        self.name = name
        self.money = money
        self.num = num
        self.pets = []
    
    def change_money(self):
        if Pet.play(): self.money-=10
        elif Pet.eat(): self.money-=5
        elif Pet.sleep(): self.money-=3






n = int(input())
for p in range(n):
    t = input().strip()

    print(t[0])
    """
    a = Person(t[0],t[1],int(t[2]))
    for i in int(t[2]):
        pet = list(input().strip())
        b = Pet(pet)
        a.pets.append(b)
    print(a)
    """
    

#m = int(input())