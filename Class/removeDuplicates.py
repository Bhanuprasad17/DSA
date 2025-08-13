

def remove_duplicates(str1):
    result = ''

    for char in str1:
        if char not in result:
            result += char

    return result

print(remove_duplicates("programming") ) # Example usage    


def remove_duplicates(input_string):
    seen = set()
    result = ''

    for char in input_string:
        if char not in seen:
            seen.add(char)
            result += char
    return result        

print(remove_duplicates("programming"))  # Example usage