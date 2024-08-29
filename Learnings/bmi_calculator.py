"""BMI calc--- Person is OW or UW
round()-----rounds to nearest value"""

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