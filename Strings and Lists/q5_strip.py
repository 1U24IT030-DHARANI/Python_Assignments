
""" Question 5: strip """
"""
Input: string s
Output: s with leading and trailing spaces removed
"""
def strip(s):
    start=0
    end=0
    for i in range(len(s)):
        if s[i]!=" ":
            start=i
            break
    for j in range(len(s)):
        if s[len(s)-1-j]!=" ":
            end=len(s)-j
            break
    return s[start:end]

""" Test 5 """
def test_strip():
    print("Testing strip...", end='')
    assert(strip("Hello") == "Hello") 
    assert(strip(" Hello world ") == "Hello world") 
    assert(strip("      apple ") == "apple") 
    assert(strip("    ") == "") 
    print("... done!")

if __name__ == '__main__':
    test_strip()