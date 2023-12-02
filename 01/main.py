NUMBER_MAP = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

def read_file(file_name):
    file_contents = ''
    with open(file_name, 'r') as file:
        file_contents = file.readlines()
    return file_contents

def run(file_contents, useWords):
    sum = 0
    for line in file_contents:
        first_digit = forward_search(line, useWords)
        last_digit = reverse_search(line, useWords)
        sum += int(first_digit + last_digit)
    return sum

def forward_search(input_string, useWords):
    if len(input_string) == 0:
        return None
    if input_string[0].isdigit():
        return input_string[0]
    if useWords:
        for key, value in NUMBER_MAP.items():
            if input_string.startswith(key):
                return value
    return forward_search(input_string[1:], useWords)

def reverse_search(input_string, useWords):
    if len(input_string) == 0:
        return None
    if input_string[-1].isdigit():
        return input_string[-1]
    if useWords:
        for key, value in NUMBER_MAP.items():
            if input_string.endswith(key):
                return value
    return reverse_search(input_string[:-1], useWords)

def outputResults(part1answer, part2answer):
    print(f'Part 1: {part1answer}')
    print(f'Part 2: {part2answer}')

def main():
    file_contents = read_file("input.txt")
    part1answer = run(file_contents, useWords=False)
    part2answer = run(file_contents, useWords=True)
    outputResults(part1answer, part2answer)

main()