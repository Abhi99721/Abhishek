def count_case_characters(input_str):
    upper_count = 0
    lower_count = 0
    for char in input_str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# Example usage
string = 'The quick Brow Fox'
upper, lower = count_case_characters(string)
print("No. of Upper case characters:", upper)
print("No. of Lower case characters:", lower)
