import random

class Warrior:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.receive_damage(damage)

    def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

def simulate_battle(warrior1, warrior2):
    while warrior1.is_alive() and warrior2.is_alive():
        warrior1.attack(warrior2)
        print(f"{warrior1.name} атакует {warrior2.name} и наносит урон {warrior1.attack_power}.")

        if not warrior2.is_alive():
            print(f"{warrior2.name} был повержен!")

        if warrior2.is_alive():
            warrior2.attack(warrior1)
            print(f"{warrior2.name} атакует {warrior1.name} и наносит урон {warrior2.attack_power}.")

        if not warrior1.is_alive():
            print(f"{warrior1.name} был повержен!")

    if warrior1.is_alive():
        print(f"{warrior1.name} побеждает!")
    elif warrior2.is_alive():
        print(f"{warrior2.name} побеждает!")
    else:
        print("Ничья!")

hero1 = Warrior(name="Герой 1", health=100, attack_power=20)
hero2 = Warrior(name="Герой 2", health=100, attack_power=18)

simulate_battle(hero1, hero2)
