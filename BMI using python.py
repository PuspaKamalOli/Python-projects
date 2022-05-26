# BMI(body mass index )=check your health if you're over/under nutrition

weight = int(input('enter your weight in kg: '))
height = int(input('enter your height in cm: '))
BMI = weight / ((height / 100) * (height / 100))
print("your BMI: " + str(BMI))
if BMI > 24.9:
    print("you're overweight, you need to lose some weight!!..")
elif BMI < 18.5:
    print("you're underweight ,you need to gain some weight!!..")
else:
    print('awesome!! you are healthy ')
