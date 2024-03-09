class Humanoid:
    def __init__(self, isAlive=True, health=100, name=""):
        self.isAlive = isAlive
        self.health = health
        self.name = name
    def kill(self):
        if self.isAlive:
            self.isAlive = False
            print(f"{self.name} is dead")
        else:
            print ("He's already dead")
    def hurt(self, damage=1):
        self.health = self.health - damage
        if self.isAlive == False:
            print("He's already dead")
        if self.health <= 0:
            print(f"{self.name}: Damn...")
            self.kill()
        if self.health > 0:
            print(f"{self.name}: " + "That hurt!")
            print(f"{self.name}'s current health: {self.health}")
    def heal(self, healing=1):
        if self.isAlive:
            self.health = self.health + healing
            print(f"{self.name}: " + "Hell yeah")
            print(f"{self.name}'s current health: {self.health}")
        else:
            print("He's dead")
    def revive(self):
        if self.isAlive == False:
            self.isAlive = True
            print(f"{self.name} has been revived!")
            self.health = 100
        else:
            print(f"{self.name}: I am already alive.")
    def stats(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nisAlive: {self.isAlive}")
            
Human1 = Humanoid(health=100, name="Steve")

Human1.hurt(10)
Human1.heal(20)
Human1.hurt(1000)
Human1.revive()
Human1.stats()