def selection_sort(l1):
    n=len(l1)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if l1[j]<l1[mini]:
                mini=j
                l1[i],l1[mini]=l1[mini],l1[i]
    return l1
l1=[24,41,33,42,17]
print(selection_sort(l1))