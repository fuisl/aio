my_string = 'Happiness'

def count_char(string):
    return {char: string.count(char) for char in string}

print(count_char(my_string))