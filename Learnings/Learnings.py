"""Swapping variables """

# a="A"
# b="B"

# temp=a
# a=b
# b=temp

# print(a)
# print(b)

"""If else work
if checks condition true, then goes to next line
if it false it goes to else block
elif: comes here:, if condition failed, it checks elif (directly not go to else
We can use logical opr AND OR NOT, if a>b and c>d for optimise
with out using elif:
    we can else: lo if else cheydm, nested IF ELSE:)"""
# a= 15
# b= 5
# c=3
# d=4
# e=5

# if a < b:
#     print("a is less than b")
#     print("fine, a is less than b")
# # print("out of if block print statement")
# else:
#     print("a is not less than b")
# if a < b:
#     print("a is less than b")
# elif b == c: #b > c:
#     print("a is greater than b")
# else:
#     print("neither of above one's are true")


"""BMI calc--- Person is OW or UW
ound rounds to nearest value"""

# Name= str(input("Enter name:"))
Name = "bunn"
height_m= float(input("Enter height in m:"))
weight_kg = float(input("Enter weight in kg:"))

# bmi =round(weight_kg/(height_m * height_m)) 
bmi = (weight_kg/(height_m * height_m))
print("bmi:")
print(bmi)
# bmi=19
if bmi<=19:
    print(f"{Name} is Underweight")
elif bmi>19 and bmi<=25:
    print(f"{Name} is normal weight")
else:
    if bmi>25 and bmi<=31 :
        print(f"{Name} is over weight")
    elif bmi>31:
        print(f"{Name} has obesity")