import random
totalIters = 10000000
totalOnes = 0
fifties = 0
for n in range(0, totalIters):
    values = [0, 1]
    for i in range(2, 100):
        values.append(random.choice(values))
    ones = 0
    for i in values:
        if i == 1:
            ones += 1
    totalOnes += ones
    if ones == 50:
        fifties += 1
print(totalOnes / totalIters)
print(fifties / totalIters)


