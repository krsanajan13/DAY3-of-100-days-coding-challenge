def insertionSort(l1):
    n=len(l1)
    for i in range(1,n):
        key=l1[i]
        j=i-1
        while j>=0 and l1[j]>key:
            l1[j+1]=l1[j]
            j-=1
        l1[j+1]=key
    return l1
l1=[23,45,21,89,12]
print(insertionSort(l1))