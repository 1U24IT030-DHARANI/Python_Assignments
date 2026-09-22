""" Question 6: recursive_mirror """
"""
Input: string s
Output: string containing s and mirror of s
        must be solved recursively
"""
def recursive_mirror(s):
    if s=="":
        return ""
    else:
        left_over_part=s[0]
        partial_result=recursive_mirror(s[1:])
        return left_over_part+partial_result+left_over_part
    

""" Test 6 """
def test_recursive_mirror():
    print("Testing recursive_mirror...", end="")
    assert(recursive_mirror("hello") == "helloolleh")
    assert(recursive_mirror("wow") == "wowwow")
    assert(recursive_mirror("code") == "codeedoc")
    assert(recursive_mirror("recursion") == "recursionnoisrucer")
    assert(recursive_mirror("") == "")
    print("... done!")

if __name__ == '__main__':
    test_recursive_mirror()
