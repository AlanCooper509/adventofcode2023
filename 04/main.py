def read_file(file_name):
    file_contents = ''
    with open(file_name, 'r') as file:
        file_contents = file.readlines()
    return file_contents

def run1(file_contents):
    points = 0
    for line in file_contents:
        winning_numbers = parse_winners(line)
        contenders = parse_contenders(line)
        points += calculate_points(winning_numbers, contenders)
    return points

def run2(file_contents):
    tickets = [1 for i in range(len(file_contents))]
    for idx, line in enumerate(file_contents):
        winning_numbers = parse_winners(line)
        contenders = parse_contenders(line)
        count = count_matches(winning_numbers, contenders)
        for offset in range(1, count+1):
            tickets[idx+offset] += tickets[idx]
    return sum(tickets)

def parse_winners(line):
    numbers = line.split(':')[1].split('|')[0].split(' ')
    return list(filter(None, numbers))

def parse_contenders(line):
    numbers = line.split(':')[1].split('|')[1].replace('\n', '').split(' ')
    return list(filter(None, numbers))

def calculate_points(winning_numbers, contenders):
    check = {}
    for winning_number in winning_numbers:
        check[winning_number] = True
    points = 0
    for contender in contenders:
        if contender in check.keys():
            points = 1 if (points == 0) else points*2
    return points

def count_matches(winning_numbers, contenders):
    check = {}
    for winning_number in winning_numbers:
        check[winning_number] = True
    points = 0
    for contender in contenders:
        if contender in check.keys():
            points += 1
    return points

def outputResults(part1answer, part2answer):
    print(f'Part 1: {part1answer}')
    print(f'Part 2: {part2answer}')

def main():
    file_contents = read_file("input.txt")
    part1answer = run1(file_contents)
    part2answer = run2(file_contents)
    outputResults(part1answer, part2answer)

main()