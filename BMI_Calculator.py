def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def bmi_category(bmi):
    if bmi < 15:
        print("Category: Severely Underweight")
        print("Advice: Consult a doctor and follow a proper meal plan to gain weight.")
    elif bmi < 18.5:
        print("Category: Underweight")
        print("Advice: Try to eat a little more and include nutritious snacks.")
    elif bmi < 25:
        print("Category: Normal weight")
        print("Advice: Keep up your healthy lifestyle!")
    elif bmi < 30:
        print("Category: Overweight")
        if bmi < 27:
            print("Advice: Watch your diet and add light exercise in your routine.")
        else:
            print("Advice: Consider regular exercise and balanced meals.")
    else:
        print("Category: Obese")
        print("Advice: Consult a doctor and follow a proper plan for weight loss.")

def main():    
    while True:
        try:
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))
            
            # Check for positive values
            if weight <= 0 or height <= 0:
                print("Weight and height must be positive numbers.\n")
                continue
            
            bmi = calculate_bmi(weight, height)
            print("\nBMI:", bmi)
            bmi_category(bmi)  # prints category and advice
            
            # Ask user if they want to continue
            a1 = input("\nDo you want to calculate again? Type y/yes to continue: ").lower()
            if a1 not in ["y", "yes"]:
                print("Thanks! Stay healthy!")
                break  # exit the loop
            print()
        except ValueError:
            print("Please enter valid numbers.\n")

if __name__ == "__main__": # fair practices, I guess!
    main()
