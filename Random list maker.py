from random import randint
import csv

result = []
for i in range(0, 1000):
    male_height = randint(175, 205)
    male_weight = randint(75, 110)
    male_shoes = randint(40, 46)
    result.append([int(male_height), int(male_weight), int(male_shoes), 'male'])
    female_height = randint(150, 178)
    female_weight = randint(50, 95)
    female_shoes = randint(35, 41)
    result.append([int(female_height), int(female_weight), int(female_shoes), 'female'])
with open('/Users/narbeh/python/AI/list.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(result)
