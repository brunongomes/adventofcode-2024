def generate_columns():
    column1, column2 = [], []
    with open('input.txt', 'r') as file:
        for line in file:
            values = line.split()
            if values:
                column1.append(int(values[0]))
                column2.append(int(values[1]))
        return column1, column2

def total_distance():
    column1, column2 = generate_columns()
    result = []
    while column1 and column2:
        min_value_column1 = min(column1)
        min_value_column2 = min(column2)
        absolute_value = abs(min_value_column1 - min_value_column2)
        result.append(absolute_value)
        column1.remove(min_value_column1)
        column2.remove(min_value_column2)
    print(f'total distance: {sum(result)}')

def similarity_score():
    column1, column2 = generate_columns()
    result = []
    for i in range(len(column1)):
        result.append(column1[i] * column2.count(column1[i]))
    print(f'similarity score: {sum(result)}')

total_distance()
similarity_score()
