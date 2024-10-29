'''
Average Time complexity - O(nlogn)
Worst Case Time Complexity - O(n2)

1. Choose the 0th index element called Pivot
2. Place it into right position, this process is called partitioning( 2 types - Hoare and Lomuto)
3. 2 subarrays are created on left and right.
4. Repeat steps 1-3 till only min(none,single) element remain in both subarrays
'''

'''
Hoare Partition

1. Start element is taken as Pivot
2. Assign 2 pointers for start and end of subarray after removing pivot
3. Move start pointer to next until the element is greater than pivot element
4. Move End pointer to previous until the element is less than pivot element
5. Swap the elemets at Start and End pointer
6. Check if end pointer is less than start pointer. If yes Stop, swap end and pivot elementd. If no, goto step 3.

Lomuto Partition

1. End Element as Pivot
2. Start element is called p-index.
3. Move p-index till element is greater than pivot element
4. Move a new counter(i-index) from p-index till element is less than pivot element
5. Swap elements at i-index and p-index.
6. If i-index is at pivot position, stop. Else repeat from step 3.

'''

def swap(a, b, arr):
  arr[a],arr[b] = arr[b],arr[a]

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)
