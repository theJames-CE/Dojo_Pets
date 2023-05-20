# Dojo Pets Assignment
    # For this assignment, you'll be asked to create a Ninja class and a Pet class.
    # Your Ninjas will be able to have a pet - and you can even practice using
    # inheritance by creating sub-classes of pets, if you're ready to stretch yourself!

class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 500
        self.energy = 100

    # implement the following methods:

# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"Minnie is asleep ZzzzZzzz", "\n")
        return self

# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.health += 10
        self.energy += 5
        print(f"Minnie eats her food and gingerly chews it with her snaggle tooth", "\n")
        return self

    def eat_treat(self):
        self.energy -= 2
        self.health += 3
        print(f"Minnie chews on her treat!", "\n", "She is a good girl!", "\n")
        return self

# play() - increases the pet's health by 5
    def walk(self):
        self.health += 5
        print(f"Taking Minnie for a trot...she loves to sniff the grass and bark at other dogs!", "\n")
        return self

    def takes_bath(self):
        self.health += 10
        self.energy -= 5
        print(f"Minnie loves baths!", "\n")
        return self

# noise() - prints out the pet's sound
    def makes_noise(self):
        self.energy -= 20
        print(f"BARK! BARK! WOOF! WOOF", "\n")
        return self

class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, pet, pet_food, treats):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.pet_food = pet_food
        self.treats = treats

    # implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.walk().makes_noise()
        return self

# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        if len(self.pet_food) > 0:
            pet_food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {pet_food}!", "\n")
            self.pet.eat()
        else:
            print("Ran out of Dog Food!", "\n")
        return self

    def give_treat(self):
        if len(self.treats) > 0:
            my_treats = self.treats.pop()
            print(f"Feeding {self.pet.name} {my_treats}!", "\n")
            self.pet.eat_treat()
        else:
            print("Ran out of Treats!", "\n")
        return self

# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
            print(f"Giving {self.pet.name} a bath", "\n")
            self.pet.takes_bath().makes_noise()


    # list of pet food & treats
my_pet_food = ["chicken wet dog food", "beef wet dog food", "chicken livers", "vegetarian dog food", "green beans", "gravy train"]
my_treats = ["Snausages", "raw hide", "rope", "Beggin strips", "pig ears", "jerky", "bone", "beef stick"]

    # defining Pet & Ninja attributes
minnie = Pet("Minnie","Dog","Playing with her Grinch Toy!","BARK! BARK! WOOF! WOOF!")
james = Ninja("James","Williams",minnie, my_pet_food, my_treats)

#Output Test
james.walk().feed().give_treat().bathe()

minnie.sleep()

print(f"Current Health: ", minnie.health)
print(f"Current Energy: ", minnie.energy)

