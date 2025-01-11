def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 24.9:
        status = "Normal weight"
    elif bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obesity"
    return bmi, status

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi, status = calculate_bmi(weight, height)
print(f"Your BMI is {bmi:.2f}. You are {status}.")
