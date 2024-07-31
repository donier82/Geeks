class Hamster:
    color = 'white'


tom = Hamster()
del tom
print(id(tom))
print(id(Hamster))
