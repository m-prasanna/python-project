def calculate_bmi(weight, height):
    # Formula for BMI: weight (kg) / (height (m))^2
    bmi = weight / (height ** 2)
    return bmi

def get_user_input():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    return weight, height

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "\033[91mUnderweight\033[0m"  # Red color for underweight
    elif 18.5 <= bmi < 24.9:
        return "\033[92mNormal weight\033[0m"  # Green color for normal weight
    elif 25 <= bmi < 29.9:
        return "\033[91mOverweight\033[0m"  # Red color for overweight
    else:
        return "\033[91mObese\033[0m"  # Red color for obese

def main():
    print("BMI Calculator")
    weight, height = get_user_input()
    
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")

    interpretation = interpret_bmi(bmi)
    print(f"Interpretation: {interpretation}")

if __name__ == "__main__":
    main()
