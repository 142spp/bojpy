input()
a = set(map(int,input().split()))
b = set(map(int,input().split()))

print(len(a.difference(b).union(b.difference(a))))