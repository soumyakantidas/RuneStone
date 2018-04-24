from random import randint


class Sort:
    def __init__(self):
        self.name = None
        self.size = 0
        self.swaps = 0
        self.comparisons = 0

    def bubble(self, arr):
        self.name = "BUBBLE"
        self.size = len(arr)
        for i in range(len(arr)-1, -1, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    self.comparisons += 1
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.swaps += 1
                else:
                    self.comparisons += 1
        return arr

    def __str__(self):
        return "sort: {}, list size: {}, comparisons: {}, swaps: {}".format(
            self.name, self.size, self.comparisons, self.swaps)


if __name__ == "__main__":
    size = 20
    li = [randint(0, 100) for _ in range(size)]
    # li = [2, 4, 1, 3, 6, 3, 4, 7, 2, 3, 1, 5, 3, 9, 0, 1, 3, 4, 8, 4]
    s = Sort()
    print(s.bubble(li))
    print(s)
