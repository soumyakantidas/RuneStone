from random import randint
from time import time
from math import log


class Sort:
    def __init__(self):
        self.name = None
        self.size = 0
        self.swaps = 0
        self.comparisons = 0
        self.time = 0

    def bubble(self, arr):
        self.name = "BUBBLE"
        self.size = len(arr)
        self.swaps = 0
        self.comparisons = 0
        self.time = 0

        t1 = time()
        for i in range(len(arr)-1, -1, -1):
            for j in range(i):
                # print(i, j)
                self.comparisons += 1
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.swaps += 1
            # print(arr)

        self.time = time() - t1
        return arr

    def bubble_short(self, arr):
        self.name = "BUBBLE-SHORT"
        self.size = len(arr)
        self.swaps = 0
        self.comparisons = 0
        self.time = 0

        t1 = time()
        exchanges = True
        i = len(arr) - 1
        while i > 0 and exchanges:
            exchanges = False
            for j in range(i):
                # print(i, j)
                self.comparisons += 1
                if arr[j] > arr[j+1]:
                    exchanges = True
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.swaps += 1
            # print(arr)
            i -= 1

        self.time = time() - t1
        return arr

    def selection(self, arr):
        self.name = "SELECTION"
        self.size = len(arr)
        self.swaps = 0
        self.comparisons = 0
        self.time = 0

        t1 = time()
        for i in range(len(arr) - 1, -1, -1):
            arg_max = i
            for j in range(i):
                self.comparisons += 1
                if arr[j] > arr[arg_max]:
                    arg_max = j
            # print(i, arg_max)
            arr[arg_max], arr[i] = arr[i], arr[arg_max]
            # print(arr)
            self.swaps += 1

        self.time = time() - t1
        return arr

    def insertion(self, arr):
        self.name = "INSERTION"
        self.size = len(arr)
        self.swaps = 0
        self.comparisons = 0
        self.time = 0

        t1 = time()
        for i in range(1, len(arr)):
            for j in range(i-1, -1, -1):
                # print(i, j)
                self.comparisons += 1
                if arr[j+1] < arr[j]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
                    self.swaps += 1
                else:
                    break
            # print(arr)

        self.time = time() - t1
        return arr

    def shell(self, arr):
        self.name = "SHELL"
        self.size = len(arr)
        self.swaps = 0
        self.comparisons = 0
        self.time = 0

        t1 = time()
        k = int(log(len(arr)+1, 2))
        gap = 2**k - 1
        # gap = len(arr)//2
        while gap > 0:
            for i in range(gap, len(arr)):
                for j in range(i-gap, -1, -gap):
                    self.comparisons += 1
                    # print("gap:", gap, "i:", i, "j:", j, "j+gap:", j+gap)
                    # print(arr[j], arr[j+gap])
                    if arr[j+gap] < arr[j]:
                        arr[j+gap], arr[j] = arr[j], arr[j+gap]
                        # print(arr)
                        self.swaps += 1
                    else:
                        break
            # gap //= 2
            k -= 1
            gap = 2**k - 1

        self.time = time() - t1
        return arr

    def merge(self, arr):
        self.name = "MERGE"
        self.size = len(arr)
        self.swaps = 0
        self.comparisons = 0
        self.time = 0

        def merge_sort(array):
            # print("Splitting ", array)
            if len(array) > 1:
                mid = len(array)//2
                left = array[:mid]
                right = array[mid:]

                merge_sort(left)
                merge_sort(right)

                i, j, k = 0, 0, 0
                while i < len(left) and j < len(right):
                    self.comparisons += 1
                    self.swaps += 1
                    if left[i] < right[j]:
                        array[k] = left[i]
                        i += 1
                    else:
                        array[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    self.swaps += 1
                    array[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right):
                    self.swaps += 1
                    array[k] = right[j]
                    j += 1
                    k += 1
                # print("Merging ", array)
            return array

        t1 = time()
        result = merge_sort(arr)
        self.time = time() - t1

        return result

    def quick(self, arr):
        self.name = "QUICK"
        self.size = len(arr)
        self.swaps = 0
        self.comparisons = 0
        self.time = 0

        def choose_pivot(array, first, last):
            mid = (first + last) // 2
            temp_list = [(array[first], first), (array[mid], mid), (array[last], last)]
            temp_list.sort(key=lambda x: x[0])
            return temp_list[1][1]

        def partition(array, first, last):
            pivot = choose_pivot(array, first, last)
            pivot_value = array[pivot]
            array[first], array[pivot] = array[pivot], array[first]
            self.swaps += 1
            pivot = first
            left = first+1
            right = last
            done = False

            while not done:
                while left <= right and array[left] <= pivot_value:
                    self.comparisons += 1
                    left += 1
                while left <= right and array[right] >= pivot_value:
                    self.comparisons += 1
                    right -= 1

                if left > right:
                    done = True
                else:
                    array[left], array[right] = array[right], array[left]
                    self.swaps += 1

            array[pivot], array[right] = array[right], array[pivot]
            self.swaps += 1

            return right

        def quick_sort(array, first, last):
            if first < last:
                split = partition(array, first, last)
                quick_sort(array, first, split-1)
                quick_sort(array, split+1, last)

        t1 = time()
        quick_sort(arr, 0, len(arr)-1)
        self.time = time() - t1
        return arr

    def __str__(self):
        return "sort: {}, list size: {}, comparisons: {}, swaps: {}, time taken: {}".format(
            self.name, self.size, self.comparisons, self.swaps, round(self.time, 6))


def partially_sort(arr, percent=80):
    arr.sort()
    distance = 20
    if percent == 100:
        percent = 99
    for i in range(len(arr)//(100//(100-percent))):
        i = randint(0, len(arr)-distance-1)
        j = randint(1, distance)
        arr[i], arr[i+j] = arr[i+j], arr[i]
    return arr


if __name__ == "__main__":
    size = 100000
    li = [randint(0, 10000) for _ in range(size)]
    # li = partially_sort(li)
    # print(li)
    # li.sort()
    # li = [10, 16, 25, 26, 27, 33, 45, 46, 46, 48, 49, 78, 60, 67, 51, 70, 88, 91, 94, 99]
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # li = [1, 3, 2, 4, 5, 5, 4, 5, 3, 4, 6, 7, 5, 8, 9, 8]
    li = [i for i in "PYTHON"]
    s = Sort()
    # s.bubble(li.copy())
    # print(s)
    # s.bubble_short(li.copy())
    # print(s)
    # s.selection(li.copy())
    # print(s)
    # s.insertion(li.copy())
    # print(s)
    # s.shell(li.copy())
    # print(s)
    print(s.merge(li.copy()))
    print(s)
    print(s.quick(li.copy()))
    print(s)
