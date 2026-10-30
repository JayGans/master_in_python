arr = [4, 2, 2, 1, 3, 4]

count = [0] * (max(arr) + 1)

for num in arr:
    count[num] += 1

result = []

for num, frequency in enumerate(count):
    result.extend([num] * frequency)

print(result)