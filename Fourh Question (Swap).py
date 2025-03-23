def swaps(A, B):
    if sorted(A) != sorted(B):
        return -1 
    
    swaps = 0
    A = list(A)
    
    for i in range(len(B)):
        if A[i] != B[i]:
            j = i
            while A[j] != B[i]:
                j += 1
            
            while j > i:
                A[j], A[j - 1] = A[j - 1], A[j]  
                swaps += 1
                j -= 1
    
    return swaps

N = int(input("Enter the length of the words: "))
A = input("Enter the original word: ")
B = input("Enter the target word: ")
print("Minimum swaps required:", swaps(A, B))

