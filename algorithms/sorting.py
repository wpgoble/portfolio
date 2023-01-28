__author__ = "William Goble"
__email__ = "will.goble@gmail.com"


def quicksort(lst):
    """
    Quicksort is a divide-and-conquer algorithm that chooses a pivot element
    from the array and partitions the other elements into two sub-arrays,
    according to whether they are less than or greater than the pivot. The
    sub-arrays are then sorted recursively.
    """
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def mergesort(lst):
    """
    Merge sort is a divide-and-conquer algorithm that divides an array in
    two, sorts the two halves, and then merges them back together.
    """
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    result = list()
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def main():
    temp = [3, 6, 8, 10, 1, 2, 1]
    print(f"Original:\t{temp}")
    print(f"Quick Sort:\t{quicksort(temp)}")
    print(f"Merge Sort:\t{mergesort(temp)}")


if __name__ == "__main__":
    main()
