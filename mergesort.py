def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        
        merge_sort(A, left, mid)
        
        merge_sort(A, mid + 1, right)
        
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    sorted_array = []
    
    i = left    
    j = mid + 1  

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted_array.append(A[i])
            i += 1
        else:
            sorted_array.append(A[j])
            j += 1
            
    while i <= mid:
        sorted_array.append(A[i])
        i += 1
        
    while j <= right:
        sorted_array.append(A[j])
        j += 1
    for k in range(len(sorted_array)):
        A[left + k] = sorted_array[k]


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("정렬 전:", arr)
    merge_sort(arr, 0, len(arr) - 1)
    
    print("정렬 후:", arr)