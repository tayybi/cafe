class Person:
    name=''
    age= ''
    height =''
    weight = ''
    def __init__(self, input_name, input_age,height,weight):
        self.name = input_name
        self.age = input_age
        self.height = height
        self.weight = weight
    
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight

    def greeting(self):
        print(f"My name is: {self.name} \n age is: {self.age} height is:{self.height} \n weight is: {self.weight}" )

jane = Person('Jane Doe', 20,  175,   150)
john = Person('John Doe', 30,  180,   160)
joe =  Person('Joe Doe',  40,  190,   170)

jane.greeting()