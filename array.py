amru,vamp  = [int(j) for j in raw_input().split(" ")]
values = [int(j) for j in raw_input().split(" ")]
sum = 0
for x in range(vamp):
	sum += values[x]
print(sum)
