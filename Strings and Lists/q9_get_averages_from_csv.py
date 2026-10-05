""" Question 9: get_averages_from_csv """
"""
Input: two strings, one representing a csv and one representing a header
Output: average of csv entries under header
        None if header does not appear in csv or if values in column are not integers
"""

def row_to_list(s):
    L = s.split(",")
    for i in range(1, len(L)):
        if (L[i].isdigit()):
            L[i] = int(L[i])
    return L
    
def csv_string_list(s):
    s = s.strip()
    stu_list = list()
    for j in s.splitlines():
        row_as_list = row_to_list(j)
        stu_list.append(row_as_list)
    return stu_list

def get_averages_from_csv(csv_str, header):  
    List=csv_string_list(csv_str)
    heading=List[0]
    data=List[1:]
    sum=0

    if header in heading[1:]:
        ind=heading.index(header)
    else:
        return None
   
    for k in data:
        sum+=k[ind]
    print("sum",sum)
    average=sum/len(data)
    print(average)
    return average

""" Test 9 """
def test_get_averages_from_csv():
    print("Testing get_averages_from_csv...", end='')
    csv = """University,Number of Students,Tuition
Carnegie Mellon University,13961,76760
Stanford University,16914,78218
Harvard University,22947,75891
University of California Berkeley,45057,41528"""
    assert(get_averages_from_csv(csv, "Number of Students") == 24719.75)
    assert(get_averages_from_csv(csv, "University") == None)
    assert(get_averages_from_csv(csv, "Tuition") == 68099.25)
    assert(get_averages_from_csv(csv, "Undergrad Population") == None)
    print("... done!")

if __name__ == '__main__':
    test_get_averages_from_csv()