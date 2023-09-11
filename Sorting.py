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

    def mergesort(self):
        def merging(arr):
            if len(arr) > 1:
                mid = len(arr)//2
                left = arr[:mid]
                right = arr[mid:]

                merging(left)
                merging(right)

                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i] <= right[j]:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
            return arr
        return merging(self.element)

    def countingsort(self):
        size = len(self.element)
        R = max(self.element) + 1
        output = [0] * size

        # Initialize count arr
        count = [0] * R

        # Store the count of each elements in count arr
        for i in range(0, size):
            count[self.element[i]] += 1

        # Store the cummulative count
        for i in range(1, R):
            count[i] += count[i - 1]

        # Find the index of each element of the original arr in count arr
        # place the elements in output arr
        i = size - 1
        while i >= 0:
            output[count[self.element[i]] - 1] = self.element[i]
            count[self.element[i]] -= 1
            i -= 1

        # Copy the sorted elements into original arr
        for i in range(0, size):
            self.element[i] = output[i]

        return self.element

    def radix_sort(lst):
        done = False
        digits = 1

        while not done:
            buckets = [[] for _ in range(10)]
            for number in lst:
                remaining_part = number // digits
                digit = remaining_part % 10
                buckets[digit].append(number)
                if remaining_part > 0:
                    done = False
                else:
                    done = True
            digits *= 10
            lst = [num for bucket in buckets for num in bucket]
        return lst
