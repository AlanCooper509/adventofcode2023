class Point():
    digit = None
    char = None
    near_symbol = None
    x = None
    y = None
    def __init__(self, i, j, char, matrix):
        self.digit = char.isdigit()
        self.char = char
        self.x = j # col specifier
        self.y = i # row specifier
        self.near_symbol = self.check_for_symbols(i, j, matrix)
    
    def check_for_symbols(self, i, j, matrix):
        if i > 0 and j > 0:
            if self.is_valid_symbol(matrix[i-1][j-1]):
                return True # top left
        if i > 0:
            if self.is_valid_symbol(matrix[i-1][j]):
                return True # top
        if i > 0 and j < len(matrix[i]) - 1:
            if self.is_valid_symbol(matrix[i-1][j+1]):
                return True # top right
        if j > 0:
            if self.is_valid_symbol(matrix[i][j-1]):
                return True # left
        if j < len(matrix[i]) - 1:
            if self.is_valid_symbol(matrix[i][j+1]):
                return True # right
        if i < len(matrix) - 1 and j > 0:
            if self.is_valid_symbol(matrix[i+1][j-1]):
                return True # bot left
        if i < len(matrix) - 1:
            if self.is_valid_symbol(matrix[i+1][j]):
                return True # bot
        if i < len(matrix) - 1 and j < len(matrix[i]) - 1:
            if self.is_valid_symbol(matrix[i+1][j+1]):
                return True # bot right
        return False
    
    def is_valid_symbol(self, char):
        return not char.isdigit() and char != '.'

def read_file(file_name):
    file_contents = ''
    with open(file_name, 'r') as file:
        file_contents = file.readlines()
    return file_contents

def run1(file_contents):
    matrix = create_matrix(file_contents)
    smart_matrix = map_surroundings(matrix)
    sum = 0
    for line in smart_matrix:
        sum += sum_valid_numbers(line)
    return sum

def run2(file_contents):
    sum = 0
    matrix = create_matrix(file_contents)
    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            if char == '*':
                sum += handle_gear(i, j, matrix)
    return sum

def create_matrix(file_contents):
    matrix = []
    for i, line in enumerate(file_contents):
        matrix.append([])
        for char in line.replace('\n', ''):
            matrix[i].append(char)
    return matrix

def map_surroundings(matrix):
    smart_matrix = []
    for i in range(len(matrix)):
        smart_matrix.append([])
        for j in range(len(matrix)):
            point = Point(i, j, matrix[i][j], matrix)
            smart_matrix[i].append(point)
    return smart_matrix

def sum_valid_numbers(line):
    sum = 0
    i = 0
    while i < len(line):
        if not line[i].digit:
            i += 1
            continue

        # start building the value reading from left to right, keep track of if any of the numbers are near a symbol
        str_number = line[i].char
        is_valid = line[i].near_symbol
        while i < len(line) - 1 and line[i+1].digit:
            i += 1
            str_number += line[i].char
            is_valid = is_valid or line[i].near_symbol
        if is_valid:
            sum += int(str_number)
        i += 1
    return sum

def handle_gear(i, j, matrix):
    top_numbers = check_above(i, j, matrix)
    side_numbers = check_sides(i, j, matrix)
    below_numbers = check_below(i, j, matrix)
    gear = top_numbers + side_numbers + below_numbers
    gear_ratio = 0
    if len(gear) == 2:
        gear_ratio = int(gear[0])*int(gear[1])
    return gear_ratio

def check_above(i, j, matrix):
    results = []
    if i < 1:
        return results

    if matrix[i-1][j].isdigit():
        part_number = scan_number(i-1, j, matrix)
        results.append(part_number)
    else:
        if j > 0 and matrix[i-1][j-1].isdigit():
            part_number = scan_number(i-1, j-1, matrix)
            results.append(part_number)
        if j < len(matrix[i]) - 1 and matrix[i-1][j+1].isdigit():
            part_number = scan_number(i-1, j+1, matrix)
            results.append(part_number)

    return results

def check_sides(i, j, matrix):
    results = []
    if j > 0 and matrix[i][j-1].isdigit():
        part_number = scan_number(i, j-1, matrix)
        results.append(part_number)
    if j < len(matrix[i]) - 1 and matrix[i][j+1].isdigit():
        part_number = scan_number(i, j+1, matrix)
        results.append(part_number)
    return results

def check_below(i, j, matrix):
    results = []
    if i >= len(matrix) - 1:
        return results

    if matrix[i+1][j].isdigit():
        part_number = scan_number(i+1, j, matrix)
        results.append(part_number)
    else:
        if j > 0 and matrix[i+1][j-1].isdigit():
            part_number = scan_number(i+1, j-1, matrix)
            results.append(part_number)
        if j < len(matrix[i]) - 1 and matrix[i+1][j+1].isdigit():
            part_number = scan_number(i+1, j+1, matrix)
            results.append(part_number)

    return results

def scan_number(i, j, matrix):
    # prerequisite
    if not matrix[i][j].isdigit():
        return None
    
    number = matrix[i][j]
    
    # check left for more digits
    leftJ = j
    while leftJ > 0 and matrix[i][leftJ-1].isdigit():
        leftJ -= 1
        number = matrix[i][leftJ] + number
    
    # check right for more digits
    rightJ = j
    while rightJ < len(matrix[i]) - 1 and matrix[i][rightJ+1].isdigit():
        rightJ += 1
        number = number + matrix[i][rightJ]
    
    return number

def outputResults(part1answer, part2answer):
    print(f'Part 1: {part1answer}')
    print(f'Part 2: {part2answer}')

def main():
    file_contents = read_file("input.txt")
    part1answer = run1(file_contents)
    part2answer = run2(file_contents)
    outputResults(part1answer, part2answer)

main()