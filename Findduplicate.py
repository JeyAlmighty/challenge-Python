numbers = [4, 7, 2, 9, 1, 7, 4, 10, 2]

dupe = []

for i in numbers:
    if numbers.count(i) > 1 and i not in dupe:
        dupe.append(i)
print(dupe)