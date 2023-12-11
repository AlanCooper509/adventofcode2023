def read_file(file_name):
    file_contents = ''
    with open(file_name, 'r') as file:
        file_contents = file.readlines()
    return file_contents

def run(file_contents):
    return ''

def outputResults(part1answer, part2answer):
    print(f'Part 1: {part1answer}')
    print(f'Part 2: {part2answer}')

def main():
    file_contents = read_file("input.txt")
    part1answer = run(file_contents)
    part2answer = run(file_contents)
    outputResults(part1answer, part2answer)

main()