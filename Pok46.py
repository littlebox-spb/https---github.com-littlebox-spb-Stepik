n, m = [int(el) for el in input().split()]
result = [[int(0) for _ in range(m)] for _ in range(n)]
li = len(result)
lj = len(result[0])
ci, cj = 0, 0
direct = 1
pointdirm = m - 1
pointdirn = n - 1
pointrot = 0

for nm in range(n * m):
    result[ci][cj] = nm + 1
    if direct == 1:
        cj += 1
        if cj > pointdirm:
            cj = pointdirm
            direct = 2
    if direct == 2:
        ci += 1
        if ci > pointdirn:
            ci = pointdirn
            direct = 3
    if direct == 3:
        cj -= 1
        if cj < pointrot:
            cj = pointrot
            pointrot += 1
            direct = 4
    if direct == 4:
        ci -= 1
        if ci < pointrot:
            pointdirm -= 1
            pointdirn -= 1
            ci = pointrot
            cj += 1
            direct = 1

for i in range(li):
    for j in range(lj):
        print(result[i][j], end=" ")
    print()


# Решение не мое, на свое я потратил 2 дня. Не смог вывести закономерность,
# что в пределах каждой диагонали совпадает сумма индексов

# n, m = [int(el) for el in input().split()]
# matrix = [[None for _ in range(m)] for _ in range(n)]
# cnt = 1

# проходим по всем диагоналям
# for d in range(n + m - 1):
#     for i in range(n):
#         for j in range(m):
#             if i + j == d:
#                 matrix[i][j] = cnt
#                 cnt += 1

# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end="")
#     print()

# i=st=0
# while i<n:
#     j=i if i<m else m
#     while j>=0:
#         st+=1
#         maxrix[i-j][j]=st
#         j-=1
#     i+=1


# for i in range(m):
#     for j in range(n):
#         print(maxrix[i][j], end=" ")
#     print()

# m, n = map(int,input().split())
# maxrix = [[0] * n for _ in range(m)]
# i=st=0
# sh=list(range(n))
# for j in range(m):
#     while i<len(sh):
#         st+=1
#         maxrix[j][i]=sh[i]+1
#         print(maxrix[j][i],end=' ')
#         i+=1
#         if i==len(sh) and i!=st:
#             i-=len(sh)
#         elif st==len(sh):
#             break
#     print()
#     i= j+1 if j<len(sh)-1 else (j+1)%len(sh)
#     st=0

# m, n = map(int,input().split())
# maxrix = [[0] * n for _ in range(m)]
# i=st=0
# for j in range(m):
#     while -1<i<n:
#         st+=1
#         maxrix[j][i]=st
#         if j%2==0:
#             i+=1
#         else:
#             i-=1
#     if i==n: i=n-1
#     if i==-1: i=0
# for j in range(m):
#     for i in range(n):
#         print(maxrix[j][i],end=' ')
#     print()


# m, n = map(int,input().split())
# maxrix = [[0] * n for _ in range(m)]
# i=st=0
# sh=list(range(n))
# for j in range(m):
#     while i<len(sh):
#         st+=1
#         maxrix[j][i]=sh[i]+1
#         print(maxrix[j][i],end=' ')
#         i+=1
#         if i==len(sh) and i!=st:
#             i-=len(sh)
#         elif st==len(sh):
#             break
#     print()
#     i= j+1 if j<len(sh)-1 else (j+1)%len(sh)
#     st=0

# n = int(input())
# maxrix = [[0] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if (i<=j and i<=n-1-j) or (i>=j and i>=n-1-j): maxrix[i][j] = 1

# for i in range(n):
#     for j in range(n):
#         print(maxrix[i][j], end=" ")
#     print()


# n = int(input())
# maxrix = [[0] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i==j or i==n-1-j: maxrix[i][j] = 1

# for i in range(n):
#     for j in range(n):
#         print(maxrix[i][j], end=" ")
#     print()


# m, n = map(int,input().split())
# maxrix = [[0] * n for _ in range(m)]
# k=1
# for i in range(n):
#     for j in range(m):
#         maxrix[j][i]=k
#         k+=1

# for i in range(m):
#     for j in range(n):
#         print(maxrix[i][j], end=" ")
#     print()


# m, n = map(int,input().split())
# k=1
# for i in range(m):
#     for j in range(n):
#         print(str(k).rjust(3), end=" ")
#         k+=1
#     print()


# n = int(input())
# maxrix = [[0] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i==j: maxrix[n-1-i][j] = 1
#         if i>n-1-j: maxrix[i][j] = 2

# for i in range(n):
#     for j in range(n):
#         print(maxrix[i][j], end=" ")
#     print()

# m, n = map(int,input().split())
# maxrix = [[' . '] * n for _ in range(m)]
# k=0
# for i in range(m):
#     for j in range(n):
#         if k%2!=0: maxrix[i][j]=' * '
#         print(maxrix[i][j].rjust(3), end=" ")
#         k+=1
#     if n!=1: k+=1
#     print()
