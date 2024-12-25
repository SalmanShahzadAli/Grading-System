# This Module Is The Combination OF The Previous Sub Modules OF InputModule
import pandas as pd
import time
import os
import numpy as np
from scipy.stats import skew

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

        
        # Prompt user for file type
        # The Below Line will Clear The Screen 
        clear_screen()
        LeaveLines()
        print("\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institue OF Engineering Sciences And Technology")
        print("\t\t\t\t\t\tFetching Data From",file_type.upper(),"Sheet")
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
        print("\t\t\t\t\t\tFile loaded successfully! Here's a structured preview of the data:")
        print("===========================================")
        print(structured_preview.head().to_string(index=False))
        print("===========================================")
        time.sleep(2)

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
    # Prompt user for file type
    # The Below Line will Clear The Screen 
    clear_screen()
    LeaveLines()
    print("\t\t\t\t\tPlease Select Between Relative And Absolute Grading")
    print("\t\t\t\t\tAbsolute Grading Means That (Fixed Grade Thresholds)")
    print("\t\t\t\t\tRelative Grading Means That (adjusting grades to match a predefined distribution like a normal curve)")
    print()
    
    # Loop until a valid input is received
    while True:
        grading_policy = input("\t\t\t\t\tPlease Enter The Name Of The Grading Policy (Relative/Absolute) (LowerCase): ").strip().lower()
        print()
        if grading_policy in ['relative', 'absolute']:
            print(f"\t\t\t\t\tYou have selected {grading_policy.capitalize()} Grading.")
            time.sleep(2)
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
    print("\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institue OF Engineering Sciences And Technology")
    print("\t\t\t\t\t\tPlease Define The Thresholds For Absolute Grading")
    print("\t\t\t\t\t\tWe Have The Following Grades [A,B,C,D,F]")
    time.sleep(2)
    clear_screen()
    LeaveLines()
    print("\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institue OF Engineering Sciences And Technology")
    # Define thresholds for absolute grading
    A = int(input("\t\t\t\t\t\tDefine Threshold For (e.g., >= 90%) A: "))
    B = int(input("\t\t\t\t\t\tDefine Threshold For (e.g., >= 80%) B: "))
    C = int(input("\t\t\t\t\t\tDefine Threshold For (e.g., >= 70%) C: "))
    D = int(input("\t\t\t\t\t\tDefine Threshold For (e.g., >= 60%) D: "))
    F = int(input("\t\t\t\t\t\tDefine Threshold For (e.g., < 60%) F: ")) # F is implicitly defined
    
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
    
    print("\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institue OF Engineering Sciences And Technology")
    print("\t\t\t\t\tGrade thresholds defined as follows:")
    for grade, threshold in thresholds.items():
        print(f"\t\t\t\t\t{grade}: >= {threshold}%")
    
    print("\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institue OF Engineering Sciences And Technology")
    print("\t\t\t\t\tFor Example IF A Student Scores More Than 90% Than He Would For Sure Get An A Grade")
    print("\t\t\t\t\tFor Example IF A Student Scores Less Than 60% Then He Would For Sure Get An F Grade")  
    time.sleep(3)      

def Grade_Threshold_Relative():
    # The Below Line will Clear The Screen 
    clear_screen()
    LeaveLines()
    print("\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institue OF Engineering Sciences And Technology")
    print("\t\t\t\t\t\tPlease Define The Grades Distributions For Relative Grading")
    print("\t\t\t\t\t\tWe Have The Following Grades [A,B,C,D,F]")
    
    time.sleep(2)
    while True:
        try:
            # The Below Line will Clear The Screen 
            clear_screen()
            LeaveLines()
            # Collecting grade distribution from the user
            print("\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institue OF Engineering Sciences And Technology")
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

def Calculate_Statistics_Relative_Grades(grades):
    # Calculate the mean of the grades
    mean = np.mean(grades)
    varaince = np.var(grades)
    skewness = skew(grades)
    return mean,varaince,skewness
def main():
    data = input_File_Type()
    # IF The user Selects relative we get returned 1 and if the user selects absolute then we get 2
    # We need to call the functions based on the inputs 
    grading_policy_number = select_grading_policy()
    # We dont need to apply validation check as its already done in the function 
    if grading_policy_number == 1:
        Grade_Threshold_Relative()
        # Extract exam scores after defining grade thresholds
        # As We Have Extracted The Data From The Files Now We Can Use The Particular Data Which We Want
        exam1_scores = data.iloc[:, 2]  # Third column for Exam 1
        exam2_scores = data.iloc[:, 3]  # Fourth column for Exam 2
        exam3_scores = data.iloc[:, 4]  # Fifth column for Exam 3

        # Calculate statistics for each exam
        exam1_stats = Calculate_Statistics_Relative_Grades(exam1_scores)
        exam2_stats = Calculate_Statistics_Relative_Grades(exam2_scores)
        exam3_stats = Calculate_Statistics_Relative_Grades(exam3_scores)
        
        # Display the results
        clear_screen()
        LeaveLines()
        print("\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institute")
        print("\t\t\t\t\tDisplaying You The Statistics Calculated For Relative Grading")
        print("\t\t\t\t\tStatistics for Exam 1: Mean = {}, Variance = {}, Skewness = {}".format(*exam1_stats))
        print("\t\t\t\t\tStatistics for Exam 2: Mean = {}, Variance = {}, Skewness = {}".format(*exam2_stats))
        print("\t\t\t\t\tStatistics for Exam 3: Mean = {}, Variance = {}, Skewness = {}".format(*exam3_stats))
    elif grading_policy_number == 2:
        Grade_Threshold_Absolute()   
    
# Example usage
if __name__ == "__main__":
    main()