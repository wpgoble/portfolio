__author__ = "William Goble"
__email__ = "will.goble@gmail.com"


def quicksort(lst):
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
