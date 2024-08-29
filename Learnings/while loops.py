"""
Loop executes as long as condtion is true
box nundi items thistunnm, 
3 items unnai box lo 
one thisinam inka 
 malli one thisinam 
 malli one thiisnm,
 no left items, exits the loop
"""

# total = 0
# for i in range(1,5):
#     # total = total +i
#     total += i
# print(total)

#OP = 10
#-----------------------------------------------------------------------------------------
# total = 0
# j = 1

# while j<5:
#     total += j
#     j += 1
#     # print(j)
# print(total)

#OP = 10
#-------------------------------------------------------------------------------------------------

#check  and print list contains only +ve numbers

# list1 = [5, 4, 4, 3, 1, -2, -3, -5] 

# total = 0
# total1 =[]
# i=0
# while list1[i]>0:
#     total += list1[i]
#     total1.append(list1[i])
#     i+= 1 
# print(total)
# print(total1)

#OP = 17  [5, 4, 4, 3, 1]

#===================================================================================
""""
if list lo anni +ve unte
iter 1 after i = 5 , list1[5]>0 ante out of index error ostadhi
to prevent that we use len of i<lenth of list or i<5
"""
# list1 = [5, 4, 4, 3, 1]  # index = 4

# total = 0
# i=0
# while i<len(list1) and  list1[i]>0:
#     total += list1[i]
#     i+= 1 
# print(total)
#OP = 17 
#=====================================================================================

#sum of itmes which >0

# list2 = [ 3,-2,8,-7,5,-6,3,1,0,1,-9,-2]

# total_sum = 0
# total_add =[]
# # for i in range(len(list2)) #desired OP not came failed!
# """ list len elemts ni thiskoni adding 1 2 3 4 5 ...12 len of list
#     iterrating i over list2 items, we take i in LIST2
#     """
# for i in list2:
#     if i>0:
#         total_sum = total_sum + i # adding and cal the sum of current i
#         total_add.append(i) # adding iter i to list to cross check

# print(total_sum) 
# print(total_add)
# 
"""
using while loop
""" 
# list2 = [3,-2,8,-7,5,-6,3,1,0,1,-9,-2]

# total_sum = 0
# total_add = []
# i=0
# # # while list2[i]>0: # loop only processed the first element because the second element in the list is -2, which caused the loop to stop.                                           
# # while i < len(list2) and list2[i] > 0:  # Continue while within bounds and the current item is positive same both lines 
# while i<len(list2):
#     if list2[i]>0:
#         total_sum += list2[i] # adding and cal the sum of current i
#         total_add.append(list2[i]) # adding iter i to list to cross check
#     i +=1

# print(total_sum)
# print(total_add)

#======================================================================================================================

