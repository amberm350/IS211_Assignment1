class ListDivideException(Exception):
    pass

def listDivide(numbers,divide = 2):
    if divide == 0:
        raise ListDivideException ("Trying to divide by 0")

    answer = 0
    for x in numbers:
        if x % divide == 0:
            answer += 1

    return answer



def testlistDivide():

    assert listDivide([1,2,3,4,5]) == 2
    assert listDivide([2,4,6,8,10]) == 5
    assert listDivide([30, 54, 63,98, 100], divide=10) == 2
    assert listDivide([]) == 0
    assert listDivide([1,2,3,4,5], 1) == 5

    
if __name__ == "__main__":
    testlistDivide()

    
