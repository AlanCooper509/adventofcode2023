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

def main():
    with open("input.txt", 'r') as file:
        sum = 0
        for line in file:
            first_digit = ''
            last_digit = ''
            first_digit = forward_search(line)
            last_digit = reverse_search(line)
            sum += int(first_digit + last_digit)
        print(sum)

def forward_search(input_string):
    if len(input_string) == 0:
        return None
    if input_string[0].isdigit():
        return input_string[0]
    for key, value in NUMBER_MAP.items():
        if input_string.startswith(key):
            return value
    return forward_search(input_string[1:])

def reverse_search(input_string):
    if len(input_string) == 0:
        return None
    if input_string[-1].isdigit():
        return input_string[-1]
    for key, value in NUMBER_MAP.items():
        if input_string.endswith(key):
            return value
    return reverse_search(input_string[:-1])

main()