
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
        
def Grade_Threshold_Relative():
    # The Below Line will Clear The Screen 
    clear_screen()
    LeaveLines()
    print("\t\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institue OF Engineering Sciences And Technology")
    print("\t\t\t\t\t\t\tPlease Define The Grades Distributions")
    print("\t\t\t\t\t\t\tWe Have The Following Grades [A,B,C,D,F]")
    
    
        