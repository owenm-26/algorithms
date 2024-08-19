# iterative approach
def iterativeBinarySearch(sortedArr, elem):
    if not sortedArr or not elem:
        raise ValueError("Inputs are undefined")
    if len(sortedArr) == 0:
        return -1
    
    front = 0
    end = len(sortedArr) -1

    # once they switch that means you've checked every relevant index
    while front <= end:
        middle = front + (end - front) // 2
        if sortedArr[middle] == elem:
            return middle
        elif elem < sortedArr[middle]:
            end = middle - 1
        else:
            front = middle + 1
    
    return -1


def recursiveBinarySearch(sortedArr, elem):
    
    # base case
    if len(sortedArr) == 0:
        return -1
    
    # recursive step
    middle = len(sortedArr) // 2
    if sortedArr[middle] == elem:
        return middle
    else:
        if sortedArr[middle] > elem:
            return recursiveBinarySearch(sortedArr[:middle], elem)
        else:
            return middle + recursiveBinarySearch(sortedArr[middle:], elem)
    

def binarySearchChecker(testRecursive=True, testIterative=True):
    array1 = [3, 8, 15, 23, 42, 56, 77] # odd num of elements
    array2 = [1, 5, 9, 12, 19, 23, 34, 45] # even num of elements
    array3 = [-21, -15, -7, 0, 4, 11, 18, 27, 33] # positives and negatives
    if testRecursive:
        assert recursiveBinarySearch(array1, 8) == 1
        assert recursiveBinarySearch(array2, 45) == len(array2)-1
        assert recursiveBinarySearch(array3, -22) == -1
        print('[RECURSIVE] All tests passed!')
    if testIterative:
        assert iterativeBinarySearch(array1, 8) == 1
        assert iterativeBinarySearch(array2, 45) == len(array2)-1
        assert iterativeBinarySearch(array3, -22) == -1
        print('[ITERATIVE] All tests passed!')
    


if __name__ == "__main__":
    binarySearchChecker()
