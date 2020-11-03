
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'AB']


def Evolve(myString):  # Executes reproduction rules
    idx = letters.index(myString) + 1
    return letters[idx % len(letters)]


generations = 20
Lsystem = 'A'
for i in range(generations):
    temp = ''
    for j in range(len(Lsystem)):
        temp = temp + Evolve(Lsystem[j])

    Lsystem = temp
    print(Lsystem)

print('number of algae')
print(len(Lsystem))
