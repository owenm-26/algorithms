def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    partition = arr.pop()
    less = []
    greater = []

    for elem in arr:
        if elem > partition:
            greater.append(elem)
        else:
            less.append(elem)
    
    return quickSort(less) + [partition] + quickSort(greater)
    

def quickSortChecker():
    # print(quickSort(random_order))
    # print(quickSort(already_sorted))
    # print(quickSort(reverse_order))
    assert quickSort(random_order) == [5, 7, 17, 23, 32, 32, 34, 62]
    assert quickSort(already_sorted)== [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert quickSort(reverse_order) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print('Quick Sort Tests Passed!')
    
if __name__ == "__main__":
    random_order = [34, 7, 23, 32, 5, 62, 32, 17]
    already_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reverse_order = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    quickSortChecker()