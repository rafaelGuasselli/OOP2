n = int(input())

prev = 1
cur = 1

print(prev)
for i in range(0, n):
    print(cur)
    prev, cur = cur, cur + prev
