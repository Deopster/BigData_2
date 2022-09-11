A = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
B = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
print(dict(zip(B,[sum(A[index] for index,i in enumerate(B,start=0) if i == el) for el in sorted(set(B))])))
