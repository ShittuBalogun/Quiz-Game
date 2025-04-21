def calculate_bmi(weight, height):
    """Calculates and returns the BMI."""
    return weight / (height ** 2)

def get_health_status(bmi):
    """Returns the health status based on BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 > bmi <= 24.9:
        return "Normal"
    elif 25 > bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    
    while True:
        try:
            weight = float(input("Enter weight in kilograms (kg): "))
            height = float(input("Enter height in meters (m): "))
            bmi = calculate_bmi(weight, height)
            status = get_health_status(bmi)

            print(f"\nYour BMI is: {bmi:.2f}")
            print(f"Health Status: {status}\n")

            # Ask if the user wants to calculate again
            repeat = input("Do you want to calculate BMI for another person? (yes/no): ").lower()
            if repeat != 'yes':
                print("Thank you for using the BMI Calculator!")
                break
        except ValueError:
            print("Please enter valid numerical values for weight and height.\n")

# Run the program
main()



    