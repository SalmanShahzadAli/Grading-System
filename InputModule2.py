# In This Module We Are Giving The Functionality To The User That
# if he has selected relative grading then he needs to specify the 
# desired grade distribution which means how many students will get 
# a particular grade
# If absolute grading is selected, allow the instructor to 
# define the grade thresholds (e.g., >=90% = A).

import time
import os


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


def main():
    Grade_Threshold_Absolute()
    

# Run the main function
if __name__ == "__main__":
    main()    