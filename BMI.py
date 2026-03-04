height = float(input("Enter your height in cm: ")) 
weight = float(input("Enter your weight in kg: "))
BMI = weight / (height/100)**2
print("Your BMI is", BMI)
if BMI <= 18.4:
    print("You're underweight. Eat more!")
elif BMI <= 24.9:
    print("You're healthy. Good job!")
elif BMI <= 29.9:
    print("You're over weight.")
elif BMI <= 34.9:
    print("You're severly overweight. Very bad!")
elif    BMI <= 39.9:
    print("You're obese. DIET!")
else:
    print("You're sumo wrestler.")