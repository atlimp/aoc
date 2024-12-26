
reports = []

with open('input', 'r') as file:
    for line in file:
        levels = list(map(int, line.split()))
        reports.append(levels)


numSafe = 0
for report in reports:
    direction = 1

    if (report[0] > report[1]):
        direction = -1

    reportIsSafe = True

    for i in range(0, len(report) - 1):
        a = report[i]
        b = report[i + 1]

        if (direction == 1 and a > b):
            reportIsSafe = False
            break

        if (direction == -1 and a < b):
            reportIsSafe = False
            break

        diff = abs(a - b)

        if (not (diff >= 1 and diff <= 3)):
            reportIsSafe = False
            break


    if reportIsSafe:
        numSafe = numSafe + 1



print(numSafe)