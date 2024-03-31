prev = 1
cur = 1

print(prev)
while cur < 500:
    print(cur)

    prev, cur = cur, cur + prev
