# In This Module We Are Giving The Functionality To The User That
# if he has selected relative grading then he needs to specify the 
# desired grade distribution which means how many students will get 
# a particular grade
# If absolute grading is selected, allow the instructor to 
# define the grade thresholds (e.g., >=90% = A).

def Grade_Threshold_Absolute():
    print("Please Define The Thresholds For Grades")
    print("We Have The Following Grades [A,B,C,D,F]")
    
    # Define thresholds for absolute grading
    A = int(input("Define Threshold For (e.g., >= 90%) A: "))
    B = int(input("Define Threshold For (e.g., >= 80%) B: "))
    C = int(input("Define Threshold For (e.g., >= 70%) C: "))
    D = int(input("Define Threshold For (e.g., >= 60%) D: "))
    F = int(input("Define Threshold For (e.g., < 60%) F: ")) # F is implicitly defined
    
    # Store thresholds in a dictionary for easy access
    thresholds = {
        'A': A,
        'B': B,
        'C': C,
        'D': D,
        'F': F,
    }
    
    print("Grade thresholds defined as follows:")
    for grade, threshold in thresholds.items():
        print(f"{grade}: >= {threshold}%")
    print("For Example IF A Student Scores More Than 90% Than He Would For Sure Get An A Grade")
    print("For Example IF A Student Scores Less Than 60% Then He Would For Sure Get An F Grade")    

def main():
    Grade_Threshold_Absolute()
    

# Run the main function
if __name__ == "__main__":
    main()    