from functools import reduce

def add (a,b):
    return a+b

print("Normal def function - ", add(5,4))

add2 = lambda a,b:a+b
print("Lambda fun - ", add2(5,4))

# lambda reduce
number = [5,-6,2,7]
total = reduce(lambda x,y : x+y , number)
print(f'The sume of the numbers is ${total}')


# sorted using lamdba

data = [(1,3),(2,1),(4,2)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)


#map
fruits = ['apple','banana','cherry']
lenghts = list(map(lambda x : len(x), fruits))
print(lenghts)

#list
list1 =[1,2,3]
list2 = [4,5,6]

result = list(map(lambda x: x[0]*x[1],zip(list1,list2)))
print(result)

#find large no among 2 nos

res = lambda x,y : x if x > y else y
print(res(4,7)) 

print(__name__)