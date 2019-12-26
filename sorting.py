from math import floor


class TreeNode():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

    def insert(self, val):
        if val < self.value:
            if not self.left:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)


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

    def bubble_recursive(self):
        sorted_array = self.array.copy()
        n = self.size

        def bubble_recursive_calls(array, n):
            if n == 1:
                return
            for i in range(n-1):
                if array[i] > array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i]
            bubble_recursive_calls(array, n-1)
        bubble_recursive_calls(sorted_array, n-1)
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

    def merge_inplace_recursive(self):
        sorted_array = self.array.copy()
        n = self.size

        def merge_recursive_calls(sorted_array, first, last):
            if first < last:
                mid = (first + last)//2

                merge_recursive_calls(sorted_array, first, mid)
                merge_recursive_calls(sorted_array, mid+1, last)

                left = first
                right = mid+1
                if sorted_array[mid] <= sorted_array[right]:
                    return
                while left <= mid and right <= last:
                    if sorted_array[left] <= sorted_array[right]:
                        left += 1
                    else:
                        temp = sorted_array[right]
                        index = right
                        while(index != left):
                            sorted_array[index] = sorted_array[index-1]
                            index -= 1
                        sorted_array[left] = temp
                        left += 1
                        mid += 1
                        right += 1

        merge_recursive_calls(sorted_array, 0, n-1)
        return sorted_array

    def tree_recursive(self):
        tree = TreeNode(self.array[0])
        n = self.size
        sorted_array = []
        for el in self.array[1:]:
            tree.insert(el)

        def inorder_traversal(root, l):

            if root:
                left = inorder_traversal(root.left, l)
                l.append(root.value)
                right = inorder_traversal(root.right, l)

        inorder_traversal(tree, sorted_array)
        return sorted_array

    def tree_iterative(self):
        print(self.array)
        tree = TreeNode(self.array[0])
        n = self.size
        sorted_array = []
        for el in self.array[1:]:
            tree.insert(el)

        stack = []
        while(True):
            while(tree):
                stack.append(tree)
                tree = tree.left
            if len(stack) == 0:
                return sorted_array
            tree = stack.pop()
            sorted_array.append(tree.value)
            tree = tree.right

    def heap_iterative(self):
        sorted_array = self.array.copy()
        n = self.size

        def heapify(array, size, root):
            largest = root
            left = 2*root+1
            right = 2*root+2

            if left < size and array[largest] < array[left]:
                largest = left
            if right < size and array[largest] < array[right]:
                largest = right

            if largest != root:
                array[root], array[largest] = array[largest], array[root]
                heapify(array, size, largest)

        for i in range(n-1, -1, -1):
            heapify(sorted_array, n, i)

        for i in range(n-1, 0, -1):
            sorted_array[i], sorted_array[0] = sorted_array[0], sorted_array[i]
            heapify(sorted_array, i, 0)
        return(sorted_array)

    def counting_iterative(self):
        sorted_array = self.array.copy()
        n = self.size

        max_item = max(sorted_array)
        count = [0] * (max_item+1)

        for elem in sorted_array:
            count[elem] += 1

        i = 0
        for j in range(len(count)):
            while(count[j] > 0):
                sorted_array[i] = j
                count[j] -= 1
                i = i+1

        return(sorted_array)

    def radix_iterative(self):
        sorted_array = self.array.copy()
        n = self.size

        def counting_sort(array, digits):
            size = len(array)
            output = [0] * size
            count = [0] * 10

            for i in range(size):
                index = array[i] // digits
                count[index % 10] += 1

            for i in range(1, 10):
                count[i] += count[i-1]

            i = size-1
            while i >= 0:
                index = array[i] // digits
                output[count[index % 10]-1] = array[i]
                count[index % 10] -= 1
                i -= 1

            for i in range(0, size):
                array[i] = output[i]

        max_item = max(sorted_array)
        digits = 1
        while max_item // digits > 0:
            counting_sort(sorted_array, digits)
            digits *= 10

        return sorted_array
