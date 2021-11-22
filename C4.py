# l = [2, 3]
# l_2 = list()
# l_2.append(1)
# l_2.append(2)
# l_2.extend([3, 4, 5])
# print(l_2)


class Coordinate(object):
    """O coordonata e compusa din valorile x, y"""

    def __init__(self, x, y):  # CONSTRUCTOR
        """Setam valorile x, y"""
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}; {self.y})'

    def distance(self, other):  # when applied, don't mention *self*
        # def __add__
        """Returnam distanta euclidiana dintre cele 2 coordonate"""
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5


origin = Coordinate(0, 0)
print(origin)

c1 = Coordinate(0, 4)
print(c1)

print(origin.distance(c1))


class Animal(object):
    def __init__(self, age):
        self.ani = age
        self.name = None

    def get_age(self):
        return self.ani

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.ani = new_age

    def set_name(self, name):
        self.name = name

    def __str__(self):  # toString()
        return f'animal: {str(self.name)} has {str(self.get_age())} years'


class Cat(Animal):
    def speak(self):
        print("meowww")

    def __str__(self):
        return f'cat: {str(self.get_name())} - has {str(self.get_age())} years'


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friends(self, friend_name):
        if friend_name not in self.get_friends():
            self.friends.append(friend_name)




scooby_doo = Animal(4)
scooby_doo.set_name('Scooby Doo')
scooby_doo.set_age(5)
print(scooby_doo)
# print(scooby_doo.bark)  # ??
print(scooby_doo.get_name())

Mira = Cat(10)
Mira.set_name("Miruca")
Mira.speak()
print(Mira)


john = Person('John', 45)
print(john)

john.add_friends('Tom')
john.add_friends('Laura')
print(john.get_friends())