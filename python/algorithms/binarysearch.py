
def binary_search(input_list, key, asc_sort=False):
    if asc_sort:
        input_list.sort()
    left = 0
    right = len(input_list) - 1
    found = False

    while left <= right and not found:
        mid = (left + right) // 2

        if input_list[mid] == key:
            found = True
        elif key < input_list[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return found


if __name__ == "__main__":
    l1 = [1, 3, 4, 7, 9]
    l2 = [3, 2, 5, 1, 8]
    print(binary_search(l1, 6))
    print(binary_search(l2, 1, True))
