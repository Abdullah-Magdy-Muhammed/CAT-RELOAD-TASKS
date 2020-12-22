n = int(input())

li = list(map(int, input().split()))

hired = untrated = 0

for elememnt in li:
    if elememnt > 0:
        hired += elememnt
        continue
    if hired > 0 and elememnt < 0:
        hired -= 1
        continue
    if elememnt < 0:
        untrated += 1

print(untrated)