document = input().rstrip()
target = input().rstrip()
count = 0

start = 0
while (i := document.find(target, start)) != -1:
    start = i+len(target)
    count += 1

print(count)
