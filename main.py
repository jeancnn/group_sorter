from random import randrange

pool = []
numberOfitems = 0
divisionNumber = 1
groupNumber = 1

numberOfitems = int(input("Number of intems (all integrants of the pool): "))
divisionNumber = int(input("Quantity of items per group (Ex: 3): "))

### Populate the list with the amount of numbers selected
for i in range(numberOfitems):
    pool.append(i+1)


while True:
    print(f"Group: {groupNumber}")
    for i in range(divisionNumber):
        aux = randrange(0,len(pool))
        print(pool[aux])
        pool.pop(aux)
    
    print('-----------------------')
    groupNumber += 1
    
    if len(pool) == 0:
        break

    if len(pool) < divisionNumber:
        print("Incomplete Group: ")
        for i in range(len(pool)):
            print(pool[i])
        break