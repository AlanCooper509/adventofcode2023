MASTER_KEY = { "red": 12, "green": 13, "blue": 14 }

def read_file(file_name):
    file_contents = ''
    with open(file_name, 'r') as file:
        file_contents = file.readlines()
    return file_contents

def run(file_contents, part1=True):
    sum = 0
    for line in file_contents:
        gameID = parse_ID(line)
        cutoffs = parse_sets(line)
        if part1:
            if is_valid(cutoffs):
                sum += gameID
        else:
            sum += calculate_power(cutoffs)
    return sum

def parse_ID(line):
    token = line.split(':')[0]
    return int(token.replace("Game ", ''))

def parse_sets(line):
    token = line.split(':')[1]
    highest_cutoffs = {}
    for set in token.split(';'):
        new_cutoffs = parse_set(set)
        highest_cutoffs = update_cutoffs(highest_cutoffs, new_cutoffs)
    return highest_cutoffs

def parse_set(set):
    cutoffs = {}
    set = set.replace('\n', '')
    for entry in set.split(','):
        tokens = entry.split(' ')
        value = int(tokens[1])
        color = tokens[2]
        cutoffs[color] = value
    return cutoffs

def update_cutoffs(highest_cutoffs, new_cutoffs):
    for key, value in new_cutoffs.items():
        if key not in highest_cutoffs.keys():
            highest_cutoffs[key] = value
            continue
        if highest_cutoffs[key] < value:
            highest_cutoffs[key] = value
    return highest_cutoffs

def is_valid(cutoffs):
    for key in cutoffs.keys():
        if cutoffs[key] > MASTER_KEY[key]:
            return False
    return True

def calculate_power(cutoffs):
    power = 1
    for value in cutoffs.values():
        power *= value
    return power

def outputResults(part1answer, part2answer):
    print(f'Part 1: {part1answer}')
    print(f'Part 2: {part2answer}')

def main():
    file_contents = read_file("input.txt")
    part1answer = run(file_contents, part1=True)
    part2answer = run(file_contents, part1=False)
    outputResults(part1answer, part2answer)

main()