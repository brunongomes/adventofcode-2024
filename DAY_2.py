def validate_security(array):
    increasing = array[1] > array[0]
    
    for i in range(len(array) - 1):
        current = array[i]
        next_value = array[i + 1]
        
        absolute_value = abs(next_value - current)
        if absolute_value < 1 or absolute_value > 3:
            return False
        
        if increasing and next_value <= current:
            return False
        if not increasing and next_value >= current:
            return False
    
    return True

def validate_with_dampener(array):
    if validate_security(array):
        return True
    
    for i in range(len(array)):
        modified_array = array[:i] + array[i+1:]
        if validate_security(modified_array):
            return True
    
    return False

def generate_data():
    with open('input.txt', 'r') as file:
        result_part1 = 0
        result_part2 = 0
        
        for line in file:
            values = line.split()
            values = list(map(int, values))
            
            if validate_security(values):
                result_part1 += 1
            
            if validate_with_dampener(values):
                result_part2 += 1
        
        print(f'first challenge: {result_part1}')
        print(f'second challenge: {result_part2}')

generate_data()
