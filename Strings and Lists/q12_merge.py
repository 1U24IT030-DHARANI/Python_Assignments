
""" Question 12: merge """
"""
Inputs: two sorted lists, A and B
Output: a sorted list combining the elements in A and B
"""
def merge(A, B):
    result=[]
    j=0
    k=0
    for i in range(len(A)+len(B)):
        if j==len(A):
            result.append(B[k])
            k+=1
        elif k==len(B):
            result.append(A[j])
            j+=1
        elif A[j]<B[k]:
            result.append(A[j])
            j+=1
        else:
            result.append(B[k])
            k+=1
    return result

""" Test 12 """
def test_merge():
    print("Testing merge...", end='')
    L1 = [1, 3, 5]
    L2 = [2, 4, 6]
    assert(merge(L1, L2) == [1, 2, 3, 4, 5, 6])
    assert(L1 == [1, 3, 5])
    assert(L2 == [2, 4, 6])
    assert(merge([1, 2, 5], [4, 6, 7]) == [1, 2, 4, 5, 6, 7])
    print("... done!")

if __name__ == '__main__':
    test_merge()