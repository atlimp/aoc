
def isSafe(report):
    direction = 1

    if (report[0] > report[1]):
        direction = -1

    for i in range(0, len(report) - 1):

        a = report[i]
        b = report[i + 1]

        if (direction == 1 and a > b):
            return (False, i)

        if (direction == -1 and a < b):
            return (False, i)

        diff = abs(a - b)

        if (not (diff >= 1 and diff <= 3)):
            return (False, i)
    
    return (True, -1)



reports = []

with open('input', 'r') as file:
    for line in file:
        levels = list(map(int, line.split()))
        reports.append(levels)


numSafe = 0
for report in reports:


    safe, i = isSafe(report)

    if (not safe):
        
        for i in range(0, len(report)):
            list = report.copy()
            list.pop(i)
            safe, _ = isSafe(list)

            if (safe):
                break

    if safe:
        numSafe = numSafe + 1



print(numSafe)