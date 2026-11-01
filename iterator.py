
# 1. What is an iterator?
# An iterator is an object that returns values one at a time.
# iter() – gets an iterator from an iterable.
# next() – gets the next value from an iterator.

numbers = [10,20,30,40]
print("***************Iterator*********************")
my_iterator = iter(numbers)

print(next(my_iterator)) #10
print(next(my_iterator)) #20
print(next(my_iterator)) #20


# 2. What is a for loop?
# A for loop automatically uses an iterator internally.
print("***************For Loop*********************")
for num in numbers:
    print(num)

# Python internally does something similar to:
print("***************For Loop internaly Iterator*********************")
my_iterator = iter(numbers)

while True:
    try:
        num = next(my_iterator)
        print(num)
    except StopIteration:
        break

# So, a for loop uses an iterator automatically.
# 3. What is a while loop?
# A while loop is simply a conditional looping statement. It does not automatically use an iterator.
print("***************While Loop*********************")
numbers = [10, 20, 30]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

#Here, we manually control the loop using an index.

#Let's create our own iterator class.
print("*********Let's create our own iterator class.********************")

class MyNumbers:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

       if self.num <= 5:
          value = self.num
          self.num += 1
          return value

       else:
           raise StopIteration

numbers = MyNumbers()
print(next(numbers))  # 1
print(next(numbers))  # 2
print(next(numbers))  # 3
print(next(numbers))  # 4
print(next(numbers))   