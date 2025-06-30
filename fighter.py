class Fighter:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.hp = 100

    def attack(self, other_fighter, damage):
        print(f"{self.name} attacks {other_fighter.name} for {damage} damage!")
        other_fighter.take_damage(damage)

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} takes {amount} damage and now has {self.hp} HP.")