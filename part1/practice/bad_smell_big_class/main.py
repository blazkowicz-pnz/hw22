class Warrior:
    def attack(self):
        ...

    def defense(self):
        ...

    def move(self):
        ...


class Healer:
    def defense(self):
        ...

    def move(self):
        ...

    def heal(self):
        ...


class Tree:
    def defense(self):
        ...

    def on_fire(self):
        ...


class Trap:
    def attack(self):
        ...


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()