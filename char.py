#Q4. Write a program to print the first non-repeated character from a string?
def char(s):
    char_count = { }
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None
input_string = "python"
result = char(input_string)
if result:
    print("The first non-repeated character is:", result)
else:
    print("No non-repeated character found in the string.")
