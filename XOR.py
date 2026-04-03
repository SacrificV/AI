import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))

px = [0] * (n + 1)

for i in range(1, n + 1):
    px[i] = px[i - 1] ^ arr[i - 1]

for _ in range(q):
    a, b = map(int, input().split())
    print(px[b] ^ px[a - 1])

### example input
#8 4
#3 2 4 5 1 1 5 3
#2 4
#5 6
#1 8
#3 3