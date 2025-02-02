#------------------------------------------------------------------

""" 
Hacker rank learnings

"""

# n = int(input().strip())

# if n%2 !=0:
#     print("Weird")
        
# if n%2==0 and 2<=n<=5:
#     print("Not Weird")
        
# if n%2==0 and 6<=n<=20:
#     print("Weird")
    
# if n%2==0 and n>20:
#     print("Not Weird")

# if (n%2 !=0) or (n%2==0 and 6<=n<=20):
#     print("Weird")

#-------------------------------------------------------------------

"""sum sub product"""

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
    
#     x = a+b
#     y = a-b
#     z = a*b
    
#     print(x)
#     print(y)
#     print(z)

#---------------------------------------------------------------------------
""" div and floor"""

# if __name__ == '__main__':
#     a = int(input()) # 4
#     b = int(input()) # 3
    
#     print(a//b) # 1
#     print(a/b) # 1.33333333

#----------------------------------------------------------------
#The list of non-negative integers that are less than n n=3 is [0,1,2] .
#  Print the square of each number on a separate line.

# if __name__ == '__main__':
#     n = int(input())
    
    
#     for i in range(0,n):
#         print(i*i)

#op =
# 0
# 1
# 4
# 9
# 16

#----------------------------------------------------------------

#leap year question 

# def is_leap(year):
#     leap = False
    
#     if year% 4==0:
        
#         if year% 100==0:
            
#             if year% 400==0:
#                 leap = True
#         else: 
#             leap = True 


#     return leap

# year = int(input())

#-------------------------------------------------------------------------------

#123...n in same line

# if __name__ == '__main__':
#     n = int(input())
    
    
#     for i in range(1,n+1):
#         print(str(i), end= '')

#__________________________________________________________________________________

# Enter your code here. Read input from STDIN. Print output to STDOUT

# T = int(input())
# for _ in range(T):

#     a, b = input().split()

#     try:
#         x = int(a)//int(b) 
#         print(x)
        
#     except ZeroDivisionError:
#         print("Error Code: integer division or modulo by zero")
        
#     except ValueError:
#         print(f"Error Code: invalid literal for int() with base 10: '{b}'", )

#---------------------------------------------------------------------------------------

# T = int(input())
# for _ in range(T):

#     a, b = input().split()

#     try:
#         x = int(a)//int(b) 
#         print(x)
        
#     except ZeroDivisionError as e:
#         print("Error Code:", e)
        
#     except ValueError as e:
#         print("Error Code:", e)

#----------------------------------------------------------------------------------------------------


    



    
    
