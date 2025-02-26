
def recursiveBinarySearch(l, num):
    length = len(l)
    middle = length//2
    if length == 0:
        return -1

    if l[middle] == num:
        return middle
    elif l[middle] > num:
        return recursiveBinarySearch(l[:middle], num)
    else:
        return middle + recursiveBinarySearch(l[middle:], num)

def iterativeBinarySearch(l, num):
    return -1

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
    binarySearchChecker(testIterative=False)