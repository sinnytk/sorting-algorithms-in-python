from math import floor


class Sorting():
    array = []
    size = 0

    def __init__(self, arr):
        self.array = arr
        self.size = len(self.array)

    def bubble_iterative(self):
        print(f'BUBBLE SORT(ITERATIVE)')

        sorted_array = self.array
        n = self.size

        for i in range(n):
            for j in range(n-1-i):
                if sorted_array[j] > sorted_array[j+1]:
                    sorted_array[j], sorted_array[j +
                                                  1] = sorted_array[j+1], sorted_array[j]
        print(f'Sorted array: {sorted_array}')
        return sorted_array

    def bubble_modified_iterative(self):
        print(f'BUBBLE MODIFIED SORT(ITERATIVE)')

        sorted_array = self.array
        n = self.size

        for i in range(n):
            swapped = False
            for j in range(n-1-i):
                if sorted_array[j] > sorted_array[j+1]:
                    sorted_array[j], sorted_array[j +
                                                  1] = sorted_array[j+1], sorted_array[j]
                    swapped = True
            if not swapped:
                break
        print(f'Sorted array: {sorted_array}')
        return sorted_array

    def selection_iterative(self):
        print(f'SELECTION SORT(ITERATIVE)')

        sorted_array = self.array
        n = self.size

        for i in range(n):
            to_replace = i
            for j in range(i+1, n):
                if sorted_array[j] < sorted_array[to_replace]:
                    to_replace = j
            sorted_array[to_replace], sorted_array[i] = sorted_array[i], sorted_array[to_replace]
        print(f'Sorted array: {sorted_array}')
        return sorted_array

    def insertion_iterative(self):
        print(f'INSERTION SORT(ITERATIVE)')

        sorted_array = self.array
        n = self.size

        for i in range(1, n):
            key = sorted_array[i]
            j = i-1
            while(j >= 0 and key < sorted_array[j]):
                sorted_array[j+1] = sorted_array[j]
                j -= 1
            sorted_array[j+1] = key
        print(f'Sorted array: {sorted_array}')

        return sorted_array

    def bucket_iterative(self):
        print(f'BUCKET SORT(ITERATIVE)')

        sorted_array = []
        n = self.size

        def insertion_sort(array):
            n = len(array)
            for i in range(1, n):
                key = array[i]
                j = i-1
                while(j > 0 and key < array[j]):
                    array[j+1] = array[j]
                    j -= 1
                array[j+1] = key
            return array

        buckets = []
        max_element = self.array[0]
        for i in range(n):
            if self.array[i] > max_element:
                max_element = self.array[i]
        for i in range(10):
            buckets.append([])
        for i in range(n):
            buckets[floor((9*self.array[i])/max_element)].append(self.array[i])
        for i in range(10):
            buckets[i] = insertion_sort(buckets[i])
            sorted_array.extend(buckets[i])
        print(f'Sorted array: {sorted_array}')
        return sorted_array
