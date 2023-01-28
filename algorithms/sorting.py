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


def main():
    temp = [3, 6, 8, 10, 1, 2, 1]
    print(f"Original:\t{temp}")
    print(f"Quick Sort:\t{quicksort(temp)}")


if __name__ == "__main__":
    main()
