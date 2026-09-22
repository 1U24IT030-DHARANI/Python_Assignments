""" Question 4: num_odd_digits """
"""
Input: integer n
Output: number of odd digits in n
"""
def num_odd_digits(n):
    counter = 0
    while(n>0):
        num = n % 10
        if(num%2!=0):
            counter += 1
        n//=10
    return counter

""" Test 4 """
def test_num_odd_digits():
    print("Testing num_odd_digits...", end='')
    assert(num_odd_digits(0) == 0)
    assert(num_odd_digits(1) == 1)
    assert(num_odd_digits(13) == 2)
    assert(num_odd_digits(2265) == 1)
    assert(num_odd_digits(2468) == 0)
    assert(num_odd_digits(13355) == 5)
    print("... done!")


if __name__ == '__main__':
    test_num_odd_digits()