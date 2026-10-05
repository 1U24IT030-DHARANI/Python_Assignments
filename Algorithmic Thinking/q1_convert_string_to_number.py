""" Question 1: convert_string_to_number """
"""
Input: string s
Output: numerical conversion of s, calculated by adding up corresponding
        letter-numbers, where a = 1, b = 2, etc. 
"""
def mapped_numbers(s):
    return ord(s) - 96
def convert_string_to_number(s):
    strings = s.lower()
    sum = 0
    for c in strings:
        map_numbers = mapped_numbers(c)
        sum += map_numbers
    return sum

""" Test 1 """
def test_convert_string_to_number():
    print("Testing convert_string_to_number...", end="")
    assert(convert_string_to_number("apple") == 50)
    assert(convert_string_to_number("Program") == 88)
    assert(convert_string_to_number("ZOOM") == 69)
    print("... done!")

if __name__ == '__main__':
    test_convert_string_to_number()