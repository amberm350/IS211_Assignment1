def listDivide(numbers,divide = 2):
    answer = 0
    for x in numbers:
        if x % divide != 0:
            pass
        else: 
            answer += 1
    return answer

class ListDivideException(Exception):
    Exception = ("Test failed")

def testlistDivide():

    assert listDivide([1,2,3,4,5]) == 2
    assert listDivide([2,4,6,8,10]) == 5
    assert listDivide([30, 54, 63,98, 101], divide=100) == 2
    assert listDivide([]) == 0
    assert listDivide([1,2,3,4,5], 1) == 5

    raise Exception
    
    
