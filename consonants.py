def consonants(string):
    def value_count(substring):
        return sum(ord(c)- ord('a') + 1 for c in substring)
    
    highest_value = 0
    current_substring = ""

    for char in string:
        if char not in 'a,e,i,o,u':
            current_substring += char
        else :
            current_value = value_count(current_substring)
            highest_value = max(highest_value, current_value)
            current_substring = ""

    current_value = value_count(current_substring)
    highest_value = max(highest_value, current_value)

