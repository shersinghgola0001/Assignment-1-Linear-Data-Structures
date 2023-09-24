#Q3. Write a program to check if two strings are a rotation of each other?
def rot_str(str1, str2):
    if len(str1) != len(str2):
        return False
    str1_double = str1 + str1
    if str2 in str1_double:
        return True
    else:
        return False
string1 = "abcde"
string2 = "cdeab"
result = rot_str(string1, string2)
if result:
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")
