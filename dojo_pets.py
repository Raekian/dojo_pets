class Ninja:
    def __init__(self, f_name, l_name, pet, treats, pet_food):
        self.f_name = f_name
        self.l_name = l_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        self.mypet = Pet("Mochi", "Shiba", "be stubborn", 50, 50)
        # self.mypet = mypet
        # self.mypet = Pet(mochi)
        # self.mypet = Pet()

    def walk(self, pet):
        print("Time for a walk!")
        self.mypet.play()

    def feed(self):
        print("Here is a", self.treats)
        self.mypet.eat()

    def bathe(self):
        print("You dork, you need a bath!")
        self.mypet.noise()

class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        print(self.name, "has", self.energy, "energy")

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} has {self.energy} energy and {self.health} health.")
        # print("has", self.energy, "energy", "and", self.health, "health")

    def play(self):
        self.health += 5
        print(self.name, "has", self.health, "health")

    def noise(self):
        print("Mochi barks")
        # if Pet() == mochi:
        #     print("Mochi barks")
        # if Pet() == miso:
        #     print("Miso Meows")


steven = Ninja("Steven", "Zerwas", "mochi", "bone", "kibbles")
mochi = Pet("Mochi", "Shiba", "be stubborn", 50, 50)
miso = Pet("Miso", "Norwegian Forest Cat", "stare menacingly", 50, 50 )


# mochi.sleep()
# mochi.play()
# mochi.eat()
# mochi.noise()
steven.walk(mochi)
print("===============")
steven.feed()
print("===============")
steven.bathe()
print("===============")
print(mochi.type)

