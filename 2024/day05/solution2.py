rules = []
updates = []

inp = '47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47'
parsing_rules = True

def parseline(line):
    global parsing_rules
    if line == '':
            parsing_rules = False
            return
        
    if parsing_rules:
        rules.append(line.split('|'))
    else:
        updates.append(line.split(','))

with open('input.txt', 'r') as file:
    for line in file:
        parseline(line.replace('\n', ''))

# for line in inp.split('\n'):
#      parseline(line)


def fixrule(update, rule):
    a_index = -1
    b_index = -1

    try:
        a_index = update.index(rule[0])
    except:
        pass

    try:
        b_index = update.index(rule[1])
    except:
        pass

    if a_index != -1 and b_index != -1 and b_index < a_index:
        update[b_index], update[a_index] = update[a_index], update[b_index]
        return True
    
    return False

def violatesrule(update, rule):
    a_index = -1
    b_index = -1

    try:
        a_index = update.index(rule[0])
    except:
        pass

    try:
        b_index = update.index(rule[1])
    except:
        pass

    if a_index != -1 and b_index != -1 and b_index < a_index:
        return True
    
    return False

def violatesany(update):
    for rule in rules:
        if violatesrule(update, rule):
            return True
    
    return False

failed = []
for update in updates:
    if violatesany(update):
        failed.append(update.copy())

print(failed)
print(len(failed))


sum = 0
for update in failed:
    passes = True
    has_violation = True
    while has_violation:
        for rule in rules:
            if violatesrule(update, rule):
                fixrule(update, rule)
        
        has_violation = violatesany(update)

            
    sum = sum + int(update[int(len(update)/2)])

          
print(sum)

