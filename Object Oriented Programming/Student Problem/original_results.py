from dataclasses import dataclass


@dataclass
class pupil():
    Name: str
    Score: int


Results = [pupil("", x + 1) for x in range(200)]

import random

for i in range(200):
    Results[i].Name = "Name" + str(i)
    Results[i].Score = random.randint(0, 100)

first = 0
second = 0
for i in range(200):
    if Results[i].Score >= first:
        first = Results[i].Score
    else:
        if Results[i].Score > second:
            second = Results[i].Score
print("Highest score was ", first)
for i in range(200):
    if Results[i].Score == first:
        print(Results[i].Name)

print("Second highest score was ", second)
for i in range(200):
    if Results[i].Score == second:
        print(Results[i].Name)