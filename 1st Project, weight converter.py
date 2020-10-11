print("This is a weight converter\nEnter your weight and we will give you the answer in either kilos or pounds")
weight= int(input("Enter your weight: "))
second_input= input("Are you in Pounds or kilograms?: ")
if second_input=="pounds":
    weight_converter= weight * 0.45
    print(f"Your weight in kilograms is {weight_converter}")
else:
    weight_converter= weight / 0.45
    print(f"your weight in pounds is {weight_converter}")