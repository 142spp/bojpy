n = int(input())
coordinates = []
for _ in range (n):
    x, y = map(int,input().split())
    coordinates.append((x,y))
s_list = sorted(coordinates,key = lambda x : (x[1],x[0]))

for e in s_list:
    print(e[0],e[1])