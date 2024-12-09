import re

def extract_mul_patterns(text):
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, text)
    return matches

def sum_of_multiplications(array):
    pattern = r"\d+"
    values = re.findall(pattern, array)
    multiplication = int(values[0]) * int(values[1])
    return multiplication

with open('input.txt', 'r') as file:
    merged_array = []
    for line in file:
        instructions = extract_mul_patterns(line)
        merged_array += instructions
    sum_of_results = 0
    for instruction in merged_array:
        result = sum_of_multiplications(instruction)
        sum_of_results += result
    print(f'add up all of the results: {sum_of_results}')