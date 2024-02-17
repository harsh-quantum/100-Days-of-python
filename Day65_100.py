class Character:
    name = None
    health = 10
    mp = 10

    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"{self.name}\nHP: {self.health}\n MP: {self.mp}")

    def setStats(self, health, mp):
        self.health = health
        self.mp = mp
class Player(Character):
    nickname = None
    lives = 3

    def __init__(self, nickname):
        self.name = "Player"
        self.nickname = nickname

    def print(self):
        print(f"{self.name}\nHP: {self.health}\nMP: {self.mp}\nNickname: {self.nickname}\nLives: {self.lives}")

    def isAlive(self):
        if self.lives > 0:
            print(f"{self.nickname} lives on!")
            return True
        else:
            print(f"{self.nickname} has expired!")
            return False

harsh = Player("Quantum hackers")
harsh.print()
print(harsh.isAlive())

class Enemy(Character):
    type = None
    strength = None

    def __init__(self, name, type, strength):
        self.name = name
        self.type = type
        self.strength = strength

    def print(self):
        print(f"\n{self.name}\nHP: {self.health}\nMP: {self.mp}\nType: {self.type}\nStrength: {self.strength}")

class Orc(Enemy):
    speed = None

    def __init__(self, speed):
        self.name = "Orc"
        self.type = "Orc"
        self.strength = 100
        self.speed = speed
    def print(self):
        print(f"\n{self.name}\nHP: {self.health}\nMP: {self.mp}\nType: {self.type}\nStrength: {self.strength}\nSpeed: {self.speed}")


sherni = Orc(150)
gray = Orc(285)
sherni.print()
gray.print()

class Vampire(Enemy):
    day = True

    def __init__(self, day):
        self.name = "Vampire"
        self.type = "Vampire"
        self.strength = 150
        self.day = day

    def print(self):
        print(f"\n{self.name}\nHP: {self.health}\nMP: {self.mp}\nType: {self.type}\nStrength: {self.strength}\nDay: {self.day}")

bishu = Vampire(True)
bishu.print()