ammu = int(raw_input())
abhi = [int(x) for x in raw_input().split(" ")]

sum = 0
for x in abhi:
	sum += x

print(sum / ammu)
