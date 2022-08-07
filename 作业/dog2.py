class Dog():

    def __init__(self,name,age):

        self.name=name

        self.age=age

    def sit(self):

        print(self.name.title()+ 'is now stting.')

    def roll_over(self):

        print(self.name.title()+ 'rolled over!')

my_dog= Dog('wille',6)

your_dog= Dog('lucy',4)

print("My dog's name is" + my_dog.name.title() + '.')

print("My dog is" + str(my_dog.age) + 'years old.')

my_dog.sit()

print("Your dog's name is" + your_dog.name.title() + '.')

print("Your dog is" + str(your_dog.age) + 'years old.')

your_dog.sit()