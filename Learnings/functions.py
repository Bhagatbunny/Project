"""
functions- collection of instructions/code
declare it and call it.
"""
# def myfucntion():
#     print("in function")
# myfucntion()
# print("outside of function")

#mapping:
"""x taking while calling parameter 3 and reutns something assing to a variable"""
# def myfucntion(x):
#     return 2*x

# a = myfucntion(3)
# print(a)
# b= myfucntion(5)
# print(b)
# def myfunction(x,y):
#     return x+y

# a= myfunction(2,3)
# print(a)

name1="A"
height_m1 = 1.5
weight_kg1 = 55

name2="B"
height_m2 = 2
weight_kg2 = 60

name3="C"
height_m3 = 2.5
weight_kg3 = 65

"""
Declaring parameters wt need sto be done
"""

def bmi_calculator(name, height_m, weight_kg): 
    bmi =round(weight_kg/(height_m * height_m))

    if bmi<=19:
        print(f"{bmi}:{name} is under weight")
    elif bmi>19 and bmi<=25:
        print(f"{bmi}:{name} is normal weight")
    else:
        if bmi>25 and bmi<=31 :
            print(f"{bmi}:{name} is over weight")
        elif bmi>31:
            print(f"{bmi}:{name} has obesity")
    return "..."
    
"""
 below passing variables to declared paramters
"""
result1 = bmi_calculator(name1,height_m1, weight_kg1) 
result2 = bmi_calculator(name2,height_m2, weight_kg2)
result3 = bmi_calculator(name3,height_m3, weight_kg3)

print(result1,result2,result3)

