

def max_number_from_string(s):

    max_num = 0
    current =''

    for char in s: 
        if char.isdigit():
            current += char
        else:
            if current:
                max_num = max(max_num, int(current))
                current = ''    
    if current:
        max_num = max(max_num, int(current))            

    return max_num    

print(max_number_from_string("abc123xyz456def789"))  # Output: 789