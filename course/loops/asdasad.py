"""
x = 2
for i in range(x): #1stloop:0 #2ndloop:1
    print("i is, ", i)
    for j in range(x): #1st:0 #2nd:1 #3rd:0 #4th:1
        print("j is, ",j)
        a = x - j + i #Results: #2 #1 #3 #2
        print(a)
"""

f = 1
A = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
for i in range(0, 3):
    print("i is",i)
    f = f * i
    print("###f is, ", f)
    for j in range(0, 3):
         print("j is",j)
         A[i][j] = f
         print(A)
print(A)