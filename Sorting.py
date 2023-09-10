class SortArray:
    def __init__(self, arr):
        self.element = arr

    def quicksort(self):
        def pivoting(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return pivoting(left) + middle + pivoting(right)
        return pivoting(self.element)

    def insertionsort(self):
        for i in range(1, len(self.element)):
            key = self.element[i]
            j = i-1
            while j >= 0 and key < self.element[j]:
                self.element[j+1] = self.element[j]
                j -= 1
            self.element[j+1] = key
        return self.element

    def shellsort(self):
        n = len(self.element)
        gap = n//2

        while gap > 0:
            for i in range(gap, n):
                temp = self.element[i]
                j = i
                while j >= gap and self.element[j-gap] > temp:
                    self.element[j] = self.element[j-gap]
                    j -= gap
                self.element[j] = temp
            gap //= 2

        return self.element
