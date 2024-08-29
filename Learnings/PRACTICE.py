# if __name__ == '__main__':
#     n = int(input().strip())
    
#     # n is odd
#     if (n%2 != 0):
#         print("Weird")
    
#     # n is even and in range 2 to 5
#     if n%2 == 0 and 2<=n<=5:
#         print("Not Weird")
        
#     else:
#         print("Not Exist in range") 

# paul_friends = ["Mary", "Tim", "Mike", "Henry"]
# tina_friends = ["Tim", "Susan", "Mary", "Josh"]
 
# combined_friends = list(set(paul_friends + tina_friends))
 
# print("Combined list of friends:", combined_friends)

#list(set()) list output with set operations(no dups)
#Combined list of friends: ['Mary', 'Mike', 'Josh', 'Tim', 'Henry', 'Susan']


#list--- dups allowed
#Combined list of friends: ['Mary', 'Tim', 'Mike', 'Henry', 'Tim', 'Susan', 'Mary', 'Josh']\

#tuple -- dups allowed
#Combined list of friends: ('Mary', 'Tim', 'Mike', 'Henry', 'Tim', 'Susan', 'Mary', 'Josh')

#set--- dups not allowed and un ordered
#Combined list of friends: {'Mike', 'Tim', 'Susan', 'Mary', 'Henry', 'Josh'}

# name = input("What is your name:")
# print(f"My name is {name} ")
# print(type(name))

# name = str(input("What is your name:"))
# print(f"My name is {name} ")
# print(type(name))


# def is_greater(a,b):
# 	if a > b:
# 		return True
# 	else:
# 		return False
	
# a= is_greater(10,5)
# print(a)


# def within_range(x):
#     if x>=10 and x<=20:
#         return True
#     else:
#         return False
# print(within_range(5))
     
# x= 10
# print(x*5)     

# Write a Python function bitwise_and(a, b) that takes two integers a and b as input and returns the result of the bitwise AND operation between them.

# def bitwise_and(a,b):
#     return a & b

# print(bitwise_and(12,5))

# thislist = ["apple", "banana", "cherry"]
# # thislist.remove(thislist.pop(0))
# thislist.remove(thislist[0])

# print(f"{thislist}")
# x = ",".join(thislist)
# print(x)

# for x in thislist:
#     print(x, end=",")

# n input, print all intergers 0 --n 
# n= int(input())
# num_list=range(n,0,-1)


# for x in num_list:
#     print(x)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = ["Melon","berry"]
 
# # fruits.extend(newlist)
# fruits=fruits+newlist
# print(fruits)


# thislist = " apple"
# mylist= thislist
# print(thislist.strip())
# print(thislist)

# print(mylist.replace("a","b"))

"""
keys - str, int, bool,
values- str, int, bool, floats
"""
    
# car = {
# "brand": 1964,
# "model": "Mustang",
# "brand": "Ford"
# }

# x = car.get("brand")

# print(type(car))   # dict
# print(type(car.keys())) # str
# print(type(car.values())) #str
# print(type(car.items())) #dict

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.model
# print(x)
    

# list1 = ["xa1", "yb2", "zc3"]
# a,b,c= list1

# # a=list1[0]
# # b=list1[1:-1]
# # # c=list1[-1]
# # print(a,b,c,d)
# #a==xa1 , 
# #c==xyz
# #b=['yb2','zc3','abc']

# for x,y,z in list1:
#     print(x,y,z)


# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# for x, obj in myfamily.items():
#     print(x)
    
#     for y in obj:
#         print(y + ':', obj[y])
        
# for x in myfamily.keys():
#     print(x)
#     new_dict = myfamily.get(x)
#     for y in new_dict.keys():
#         print(f"{y} {new_dict.get(y)}")

# for x in myfamily:
#     print(x)
#     new_dict = myfamily.get(x)
#     for y in new_dict:
#         print(f"{y} {new_dict.get(y)}")
    


# a = ["a","b"]
# x=a.reverse()
# print(a)
# a = a*5
# print(a)





#n is an whole num
#print square of stars with each side having n stars

# n = int(input())
# for _ in range(n):
#     print("*" * n)

# n = int(input())

# for i in range(1,n+1):
#     print("*"*i)
    
# *###* for n?

# n = int(input())
# for i in range(n):
#     # print(f"*","#","*") #n=3
#     # print(f"*","#"*2,"*") #n=4
#     # print("*","#"*(n-2),"*")  #n=5
#     # print("*","#"*(n-2),"*",sep='') # it also works
#     print("*"+"#"*(n-2)+"*") # by concating th string

# 1
# 12
# 123
# 1234?

# n= int(input())

# for i in range(1,n+1):
#     for j in range(1,i+1):

#         print(j, end="") # end=""   new line ki velladhu , print beise like 12
#     print()
    
#equilateral triangle?

# n= int(input())#=5

# for i in range(1,n+5,2):
#     print('@'*(n-i), '* '*i)

#123
#456
#789

n= int(input())#=5

for i in range(1,n):
    for j in range(n):
        print(j+1, end="")
    print()


    
      
    
    

    


    



