def mergeSort(arr):

    # base case
    if len(arr) <= 1:
        return arr
    
    middle = 0 + (len(arr))//2
    left = mergeSort(arr[middle:])
    right = mergeSort(arr[:middle])

    return merge(left, right)

def merge(left, right):
    result = []
    l = 0
    r = 0

    # zipper them into one another
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    
    # add the rest of the elements from the array that isn't empty
    result.extend(left[l:])
    result.extend(right[r:])

    return result

def mergeSortChecker():
    # print(mergeSort(sorted_array))
    # print(mergeSort(reverse_sorted_array))
    # print(mergeSort(random_array))
    assert mergeSort(sorted_array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert mergeSort(reverse_sorted_array) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert mergeSort(random_array) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    print('Merge Sort Tests Passed!')

if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reverse_sorted_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    random_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    mergeSortChecker()