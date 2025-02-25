def calculate_score(ingredients, v):
    product = 1

    for i in range(len(ingredients[0])):
        sum = 0

        for j in range(len(v)):
            sum += v[j] * ingredients[j][i]

        if (sum < 0):
            return 0

        product *= sum

    return product

def get_seq(max, parts):
    solutions = []

    if (parts < 0):
        return []

    if max == 0:
        solutions.append([0] * parts)

    for i in range(max, -1, -1):
        one_down = get_seq(max - i, parts - 1)

        for list in one_down:
            sol = [i]
            sol.extend(list)
            solutions.append(sol)
    
    return solutions

with open('input') as file:
    lines = file.read().split('\n')

    ingredients = []
    
    for line in lines:
        _, properties = line.split(': ')
        scores = []
        for property in properties.split(', '):
            _, score = property.split(' ')
            if (_ != 'calories'):
                scores.append(int(score))
        
        ingredients.append(scores)

max_score = 0
max_seq = []
for seq in get_seq(100, len(ingredients)):
    score = calculate_score(ingredients, seq)
    if max_score < score:
        max_score = score
        max_seq = seq


print(max_score)
print(max_seq)


    
