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

    def insertion_iterative(self):
        print(f'INSERTION SORT(ITERATIVE)')

        sorted_array = self.array
        n = self.size

        for i in range(1, n):
            key = sorted_array[i]
            j = i-1
            while(j > 0 and key < sorted_array[j]):
                sorted_array[j+1] = sorted_array[j]
                j -= 1
            sorted_array[j+1] = key
        print(f'Sorted array: {sorted_array}')
