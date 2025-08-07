def bubbleSort(l1):
    n=len(l1)
    for i in range(n):
        for j in range(0,n-i-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1]=l1[j+1],l1[j]

    return l1

l1=[23,45,67,43,90,1]
print(bubbleSort(l1))