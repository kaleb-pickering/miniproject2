class Dog:
    def __init__(self, age, name, is_male, weight):
        self.age = age
        self.name = name
        self.is_male = is_male # Boolean. True if Male, False if Female.
        self.weight = weight

my_dog = Dog(1,"Moe", False , 5)
print(f"Hellow, my dog's name is {my_dog.name}, her age is {my_dog.age}, and her weight is {my_dog.weight}. ")

your_dog = Dog(11,"Eva", False , 35)
print(f"Hellow, my dog's name is {your_dog.name}, her age is {your_dog.age}, and her weight is {your_dog.weight}. ")