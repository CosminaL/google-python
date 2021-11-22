class Fractie(object):
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f'{self.numarator}/{self.numitor}'

    def __add__(self, other):
        numarator_2 = self.numarator * other.numitor + self.numitor * other.numarator
        numitor_2 = self.numitor * other.numitor
        return Fractie(numarator_2, numitor_2)

    def __sub__(self, other):
        numarator_2 = self.numarator * other.numitor - self.numitor * other.numarator
        numitor_2 = self.numitor * other.numitor
        return Fractie(numarator_2, numitor_2)

    def inverse(self):
        return Fractie(self.numitor, self.numarator)


fr_1 = Fractie(3, 4)
print(fr_1)

fr_2 = Fractie(4, 5)

fr_sum = fr_1.__add__(fr_2)
print(fr_sum)

fr_diff = fr_1.__sub__(fr_2)
print(fr_diff)

fr_inv = fr_1.inverse()
print(fr_inv)




# __add__ return o noua instanta de fractie numarator/numitor

# f1.inverse() => a new object Fractie
