from random import randint
from time import time


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

    def __str__(self):
        return "sort: {}, list size: {}, comparisons: {}, swaps: {}, time taken: {}".format(
            self.name, self.size, self.comparisons, self.swaps, round(self.time, 6))


def partially_sort(arr, percent=80):
    arr.sort()
    distance = 20
    if percent == 100:
        percent = 99
    for i in range(len(arr)//(100//(100-percent))):
        i = randint(0, len(arr)-distance)
        j = randint(1, distance)
        arr[i], arr[i+j] = arr[i+j], arr[i]
    return arr


if __name__ == "__main__":
    size = 4000
    li = [randint(0, 10000) for _ in range(size)]
    # li = partially_sort(li, 90)
    # print(li)
    # li.sort()
    # li = [10, 16, 25, 26, 27, 33, 45, 46, 46, 48, 49, 78, 60, 67, 51, 70, 88, 91, 94, 99]
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # li = [1, 3, 2, 4, 5, 5, 4, 5, 3, 4, 6, 7, 5, 8, 9, 8]
    s = Sort()
    print(s.bubble(li.copy()))
    print(s)
    print(s.bubble_short(li.copy()))
    print(s)
    print(s.selection(li.copy()))
    print(s)
    print(s.insertion(li.copy()))
    print(s)
