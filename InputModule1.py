# in this module we are giving the user an option to 
# select between relative and absolute grading

def select_grading_policy():
    print("Please Select Between Relative And Absolute Grading")
    print()
    
    # Loop until a valid input is received
    while True:
        grading_policy = input("Please Enter The Name Of The Grading Policy (Relative/Absolute): ").strip().lower()
        print()
        if grading_policy in ['relative', 'absolute']:
            print(f"You have selected {grading_policy.capitalize()} Grading.")
            break  # Exit the loop if valid input is received
        else:
            print("Invalid input. Please enter 'Relative' or 'Absolute'.")

def main():
    select_grading_policy()

# Run the main function
if __name__ == "__main__":
    main()

