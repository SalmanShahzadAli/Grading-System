# This Module Is The Combination OF The Previous Sub Modules OF InputModule
import pandas as pd
import time
import os


def input_File_Type():
    """Allow the user to choose the file type and load grades accordingly."""
    try:
        # Prompt user for file type
        # The Below Line will Clear The Screen 
        clear_screen()
        LeaveLines()
        print("\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institue OF Engineering Sciences And Technology")
        file_type = input("\t\t\t\t\t\tEnter the file type (CSV/Excel): ").strip().lower()
        if file_type not in ["csv", "excel"]:
            raise ValueError("\t\t\t\t\t\tInvalid file type. Please enter 'CSV' or 'Excel'.")

        # Prompt user for file path
        file_path = input("\t\t\t\t\t\tEnter the path to the file: ").strip()

        # Load file based on type
        if file_type == 'csv':
            data = pd.read_csv(file_path)
        elif file_type == 'excel':
            data = pd.read_excel(file_path)

        print()
        print("Fetching Data From",file_type.upper(),"Sheet")
        # Validate required columns
        if len(data.columns) < 5:
            raise ValueError("The file must contain at least 5 columns: FirstName, LastName, and three exam scores.")

        # Define the sections explicitly
        sections = {
            "First Name": data.iloc[:, 0],  # First column
            "Last Name": data.iloc[:, 1],  # Second column
            "Exam 1": data.iloc[:, 2],     # Third column
            "Exam 2": data.iloc[:, 3],     # Fourth column
            "Exam 3": data.iloc[:, 4]      # Fifth column
        }

        # Combine sections into a structured DataFrame
        structured_preview = pd.DataFrame(sections)

        # Display a structured preview
        print("\nFile loaded successfully! Here's a structured preview of the data:")
        print(structured_preview.head().to_string(index=False))

        return data
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        return None
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

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


def LeaveLines():
    print("\n" * 15)
def clear_screen():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')

def Grade_Threshold_Absolute():
    # The Below Line will Clear The Screen 
    clear_screen()
    LeaveLines()
    print("\t\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institue OF Engineering Sciences And Technology")
    print("\t\t\t\t\t\t\tPlease Define The Thresholds For Grades")
    print("\t\t\t\t\t\t\tWe Have The Following Grades [A,B,C,D,F]")
    
    # Define thresholds for absolute grading
    A = int(input("\t\t\t\t\t\t\tDefine Threshold For (e.g., >= 90%) A: "))
    B = int(input("\t\t\t\t\t\t\tDefine Threshold For (e.g., >= 80%) B: "))
    C = int(input("\t\t\t\t\t\t\tDefine Threshold For (e.g., >= 70%) C: "))
    D = int(input("\t\t\t\t\t\t\tDefine Threshold For (e.g., >= 60%) D: "))
    F = int(input("\t\t\t\t\t\t\tDefine Threshold For (e.g., < 60%) F: ")) # F is implicitly defined
    
    # Store thresholds in a dictionary for easy access
    thresholds = {
        'A': A,
        'B': B,
        'C': C,
        'D': D,
        'F': F,
    }
    time.sleep(2)
    clear_screen()
    LeaveLines()
    
    print("\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institue OF Engineering Sciences And Technology")
    print("\t\t\t\t\t\t\tGrade thresholds defined as follows:")
    for grade, threshold in thresholds.items():
        print(f"\t\t\t\t\t\t\t{grade}: >= {threshold}%")
    
    time.sleep(3)    
    
    clear_screen()
    LeaveLines()    
    print("\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institue OF Engineering Sciences And Technology")
    print("\t\t\t\t\t\tFor Example IF A Student Scores More Than 90% Than He Would For Sure Get An A Grade")
    print("\t\t\t\t\t\tFor Example IF A Student Scores Less Than 60% Then He Would For Sure Get An F Grade")    

def Grade_Threshold_Relative():
    # The Below Line will Clear The Screen 
    clear_screen()
    LeaveLines()
    print("\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institue OF Engineering Sciences And Technology")
    print("\t\t\t\t\t\tPlease Define The Grades Distributions")
    print("\t\t\t\t\t\tWe Have The Following Grades [A,B,C,D,F]")
    
    time.sleep(2)
    while True:
        try:
            # The Below Line will Clear The Screen 
            clear_screen()
            LeaveLines()
            # Collecting grade distribution from the user
            a = float(input("\t\t\t\t\tEnter the percentage of students receiving grade A (e.g., 20%): "))
            b = float(input("\t\t\t\t\tEnter the percentage of students receiving grade B (e.g., 30%): "))
            c = float(input("\t\t\t\t\tEnter the percentage of students receiving grade C (e.g., 25%): "))
            d = float(input("\t\t\t\t\tEnter the percentage of students receiving grade D (e.g., 15%): "))
            f = float(input("\t\t\t\t\tEnter the percentage of students receiving grade F (e.g., 10%): "))
            time.sleep(2)
            # The Below Line will Clear The Screen 
            clear_screen()
            LeaveLines()
            # Validate the total percentage
            total = a + b + c + d + f
            if total != 100:
                print("Error: The total percentage must equal 100%. Please try again.")
            else:
                print("\t\t\t\t\tGrade distribution defined successfully!")
                print(f"\t\t\t\t\tA: {a}%, B: {b}%, C: {c}%, D: {d}%, F: {f}%")
                print(f"\t\t\t\t\tFor Example {a}% students will get an A grade")
                print(f"\t\t\t\t\tFor Example {f}% students will get an F grade")
                break  # Exit the loop if the input is valid
        except ValueError:
            print("Error: Please enter valid numerical values.")


def main():
    input_File_Type()
    # IF The user Selects relative we get returned 1 and if the user selects absolute then we get 2
    # We need to call the functions based on the inputs 
    grading_policy_number = select_grading_policy()
    # We dont need to apply validation check as its already done in the function 
    if grading_policy_number == 1:
        Grade_Threshold_Relative()
    elif grading_policy_number == 2:
        Grade_Threshold_Absolute()   
    
# Example usage
if __name__ == "__main__":
    input_File_Type()