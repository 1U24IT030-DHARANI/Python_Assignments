""" Question 4: count """
"""
Inputs: two strings, s and t
Output: number of times t occurs in s
"""

from q1_starts_with import starts_with 

def count(s, t):
    count=0
    i=0
    while(len(s)>i):
        if starts_with(s,t,i):
            count+=1  
            i+=len(t)  
        else:
            i+=1
    return count

""" Test 4 """
def test_count():
    print("Testing count...", end='')
    assert(count("Hello", "l") == 2)
    assert(count("pineapple", "p") == 3)
    assert(count("farewell everyone", "are") == 1)
    assert(count("", "aa") == 0)
    assert(count("Hello world", " ") == 1)
    print("... done!")

if __name__ == '__main__':
    test_count()