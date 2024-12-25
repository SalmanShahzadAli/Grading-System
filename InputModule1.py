# in this module we are giving the user an option to 
# select between relative and absolute grading

def select_grading_policy():
    print("Please Select Between Relative And Absolute Grading")
    print("Absolute Grading Means That (Fixed Grade Thresholds)")
    print("Relative Grading Means That (adjusting grades to match a predefined distribution like a normal curve)")
    print()
    
    # Loop until a valid input is received
    while True:
        grading_policy = input("Please Enter The Name Of The Grading Policy (Relative/Absolute): ").strip().lower()
        print()
        if grading_policy in ['relative', 'absolute']:
            print(f"You have selected {grading_policy.capitalize()} Grading.")
            if grading_policy == "relative":
                return 1
            elif grading_policy == "absolute":
                return 2
        else:
            print("Invalid input. Please enter 'Relative' or 'Absolute'.")

def main():
    number = select_grading_policy()
    print("Number = ",number)

# Run the main function
if __name__ == "__main__":
    main()

