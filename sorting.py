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
