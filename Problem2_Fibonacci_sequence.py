fibonacci = [0, 1]
total = 0

while fibonacci[-1] < 4000000:
	fibonacci.append(fibonacci[-1]+fibonacci[-2])

for num in fibonacci:
	if num < 4000000 and num%2 ==0:
		total += num

print(total)




