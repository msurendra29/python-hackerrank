n = int(input())
mylist = input().strip().split()
print(mylist)
mylist = [int(i) for i in mylist]
print(mylist)
t = tuple(mylist[0:n:1])
print(t)
print()
print(hash(t))


