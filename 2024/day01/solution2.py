
list1 = []
list2 = []

with open('input', 'r') as file:
    for line in file:
        nrs = line.split()
        list1.append(int(nrs[0]))
        list2.append(int(nrs[1]))

list1.sort()
list2.sort()

similarity = 0
for i in range(0, len(list1)):
    a = list1[i]

    count = 0
    for candidate in list2:
        if (a == candidate):
            count = count + 1
    


    similarity = similarity + abs(a * count)

print(similarity)