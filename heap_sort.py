import heapq

arr= [5,3,8,1,2]
heapq.heapify(arr)

result =[]

while arr:
    result.append(-heapq.heappop(arr)) if False else result.append(heapq.heappop(arr))

print(result)