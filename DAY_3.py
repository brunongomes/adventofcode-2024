import re

def extract_patterns(pattern, text):
    return re.findall(pattern, text)

def calculate_multiplication(expression):
    numbers = extract_patterns(r"\d+", expression)
    return int(numbers[0]) * int(numbers[1])

def process_file(file_path):
    instructions = []
    with open(file_path, 'r') as file:
        for line in file:
            instructions.extend(extract_patterns(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", line))
    return instructions

def sum_of_multiplications(file_path):
    instructions = []
    with open(file_path, 'r') as file:
        for line in file:
            instructions.extend(extract_patterns(r"mul\(\d+,\d+\)", line))
    total = sum(calculate_multiplication(instruction) for instruction in instructions)
    print(f'add up all of the results: {total}')

def do_dont_logic(file_path):
    instructions = process_file(file_path)
    status = True
    total = 0
    for instruction in instructions:
        if instruction == "do()":
            status = True
        elif instruction == "don't()":
            status = False
        elif "mul" in instruction and status:
            total += calculate_multiplication(instruction)
    print(f'add up all of the results with do and dont: {total}')

file_path = 'input.txt'
sum_of_multiplications(file_path)
do_dont_logic(file_path)
