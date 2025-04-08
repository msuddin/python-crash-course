class Dog:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.owner = f'{self.name}' # Default value

    # Methods
    def sit(self):
        print(f'\n{self.name} is now sitting')

    def roll_over(self):
        print(f'{self.name} is now rolling over')

    def get_owner(self):
        print(f'{self.owner} is the current owner')

    def set_owner(self, new_owner):
        self.owner = new_owner
        print(f'Changed owner to {self.owner}')

my_dog = Dog('My Dog', 20)
my_dog.sit()
my_dog.roll_over()
my_dog.get_owner()

my_friends_dog = Dog('My Friends Dog', 20)
my_friends_dog.sit()
my_friends_dog.roll_over()
my_friends_dog.get_owner()
my_friends_dog.owner = 'Random Owner' # Possible to change the owner via class variable
my_friends_dog.get_owner()
my_friends_dog.set_owner('My Cousins Dog')
my_friends_dog.get_owner()