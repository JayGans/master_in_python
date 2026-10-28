#file I/O read write delete
import os
 

#Types of all files

#1. Text Files : .txt, .docx, .log etc
#2. Binary Files: .mp4, .mov, .png, .jpeg etc.
#f = open("sample.txt","a") # with open('sample.txt',"r+") as f:
#data = f.read()
# readsingleline = f.readline()
# print(readsingleline)
# #print(data)
# #print(type(data))
# f.close()

# f.write("\ni will do what i need to do to achive this")
# f.close()

# remove file 
# os.remove('sample.txt')

# with open('sample.txt','w') as f:
#     f.write('Hi everyone\nwe are learning File I/O\n')
#     f.write('write Java.\nI like programming in Java')

#WAP read data and replay java with python in file
# with open('sample.txt','r') as f:
#     data =f.read()

# new_data=data.replace("Java","Python")
# print(new_data)

# with open('sample.txt','w') as f:
#     f.write(new_data)

#WAP search the word 'learning' exists in the file or not 

# with open('sample.txt','r') as f:
#     data= f.read()
#     isWord=  data.find('learning')
#     if isWord!=-1:
#         print('Found')
#     else:
#         print('no found')

# def check_for_line():
#     word = "learning"
#     data =True
#     line_no =1
#     with open('sample.txt','r') as f:
#         while data:
#            data = f.readline()
#            if word in data:
#                print(line_no)
#                return
#            line_no+=1
#     return -1  
        
# check_for_line()

def get_even_no_count():

    with open('sample.txt','w') as f:
        f.write("1,2,76,84,90,101")

    with open('sample.txt','r') as f:
        data = f.read()

    numbers = data.split(",")
    even_count=0
    for num in numbers:
        if int(num)%2 == 0:
            even_count+=1


    print(even_count)    

get_even_no_count()