# def sum(a,b):
#     c = a+b
#     return c

# s= sum(1,2) #function call
# print(s)

#WAP to print lenghth of list

# def list_len(list):
#     print(len(list))

# l=['nagapur','pune','nagar']
# list_len(l)   
# 

#WAP print list elements in single line  

# def list_ele(list):
#     for ele in list:
#         print(ele, end=",")

# names = ['ganesh','amit','sagar']

# list_ele(names)

#WAP factorial no 

# def fact(n):
#     if n==0 or n==1:
#         return n
#     return n * fact(n-1)

# f= fact(5)
# print(f)

# def conveter(usd_val):
#     inr =usd_val*85
#     print(usd_val, "USD =", inr, "INR")

# conveter(300)

#Recursion
#function call itself repeatedly
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1) # calling same function

# show(5)    

# def cal_sum(n):
#     if n==0:
#         return 0
#     return cal_sum(n-1) + n

# sum = cal_sum(5)
# print(sum)    

#WAP print all ele from list

# def ele_list(list, idx):
#     if idx==len(list):
#         return
#     print(list[idx])
#     ele_list(list,idx+1)

# ele_list(["amit","ganesh"],0)
