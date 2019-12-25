from math import floor


class Sorting():
    array = []
    size = 0

    def __init__(self, arr):
        self.array = arr
        self.size = len(self.array)

    def bubble_iterative(self):
        print(f'BUBBLE SORT(ITERATIVE)')

        sorted_array = self.array.copy()
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

        sorted_array = self.array.copy()
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

        sorted_array = self.array.copy()
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

        sorted_array = self.array.copy()
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

    def merge_iterative(self):
        sorted_array = self.array.copy()
        n = self.size

        def merge(a, l, m, r):
            n1 = m - l + 1
            n2 = r - m
            L = [0] * n1
            R = [0] * n2
            for i in range(0, n1):
                L[i] = a[l + i]
            for i in range(0, n2):
                R[i] = a[m + i + 1]

            i, j, k = 0, 0, l
            while i < n1 and j < n2:
                if L[i] > R[j]:
                    a[k] = R[j]
                    j += 1
                else:
                    a[k] = L[i]
                    i += 1
                k += 1

            while i < n1:
                a[k] = L[i]
                i += 1
                k += 1

            while j < n2:
                a[k] = R[j]
                j += 1
                k += 1

        current_size = 1
        while current_size < len(sorted_array) - 1:

            left = 0
            while left < len(sorted_array)-1:
                mid = left + current_size - 1
                right = ((2 * current_size + left - 1,
                          len(sorted_array) - 1)[2 * current_size
                                                 + left - 1 > len(sorted_array)-1])
                merge(sorted_array, left, mid, right)
                left = left + current_size*2
            current_size = 2 * current_size

        return sorted_array

    def merge_recursive(self):
        sorted_array = self.array.copy()
        n = self.size

        def merge_recursive_calls(sorted_array, n):
            if n > 1:
                mid = n//2
                left = sorted_array[:mid]
                right = sorted_array[mid:]

                merge_recursive_calls(left, len(left))
                merge_recursive_calls(right, len(right))

                i = j = k = 0
                while j < len(left) and k < len(right):
                    if left[j] < right[k]:
                        sorted_array[i] = left[j]
                        j += 1
                    else:
                        sorted_array[i] = right[k]
                        k += 1
                    i += 1
                while j < len(left):
                    sorted_array[i] = left[j]
                    i += 1
                    j += 1
                while k < len(right):
                    sorted_array[i] = right[k]
                    i += 1
                    k += 1

        merge_recursive_calls(sorted_array, n)
        return sorted_array

    def quick_recursive(self):
        sorted_array = self.array.copy()
        n = self.size

        def partition(arr, l, h):
            pivot = arr[h]
            i = l
            for j in range(l, h):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i = i+1
            arr[i], arr[h] = arr[h], arr[i]
            return i

        def quick_sort(arr, l, h):
            if l < h:
                pivot = partition(arr, l, h)
                quick_sort(arr, l, pivot-1)
                quick_sort(arr, pivot+1, h)
        quick_sort(sorted_array, 0, n-1)
        return sorted_array

    def quick_iterative(self):
        sorted_array = self.array.copy()
        n = self.size

        def partition(arr, l, h):
            pivot = arr[h]
            i = l
            for j in range(l, h):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i = i+1
            arr[i], arr[h] = arr[h], arr[i]
            return i

        l = 0
        h = n-1
        stack = [None] * (n)

        stack.append(l)
        stack.append(h)
        while(stack[-1]):
            h = stack.pop()
            l = stack.pop()
            pivot = partition(sorted_array, l, h)

            if pivot-1 > l:
                stack.append(l)
                stack.append(pivot-1)
            if pivot+1 < h:
                stack.append(pivot+1)
                stack.append(h)
        return sorted_array

    def shell_iterative(self):
        sorted_array = self.array.copy()
        n = self.size
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = sorted_array[i]
                j = i
                while j >= gap and sorted_array[j - gap] > temp:
                    sorted_array[j] = sorted_array[j - gap]
                    j -= gap
                sorted_array[j] = temp
            gap //= 2
        return sorted_array
