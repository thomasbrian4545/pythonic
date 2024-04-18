# List comprehension dan if

listku = [10,70,30,50]
""" listmu = []

for item in listku:
    if item > 50:
        listmu.append(item)
 """
listmu = [item for item in listku if item < 50]

print(f"listku : {listku}")
print(f"listmu : {listmu}")