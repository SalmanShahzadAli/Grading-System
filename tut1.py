import csv
import numpy as np
from scipy.stats import skew, rankdata
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time

# The below function is there to just validate the inputs that weather they are float or not
def get_float_input(prompt, min_value=0, max_value=100):
    """Validates if the input is a float and within a given range."""
    while True:
        try:
            value = float(input(prompt))
            if value < min_value or value > max_value:
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def get_distribution_input():
    """Ensures the sum of A, B, C, and D percentages is equal to 1."""
    while True:
        distribution = {
            'A': get_float_input("\t\t\t\t\t\tEnter percentage for A (e.g., 0.10 for 10%): ", 0, 1),
            'B': get_float_input("\t\t\t\t\t\tEnter percentage for B (e.g., 0.20 for 20%): ", 0, 1),
            'C': get_float_input("\t\t\t\t\t\tEnter percentage for C (e.g., 0.30 for 30%): ", 0, 1),
            'D': get_float_input("\t\t\t\t\t\tEnter percentage for D (e.g., 0.40 for 40%): ", 0, 1),
        }
        # Validate if the sum is equal to 1
        if sum(distribution.values()) == 1:
            return distribution
        else:
            print("Error: The sum of the percentages must be equal to 1. Please try again.")            
def calculate_statistics(scores):
    """Calculates and returns mean, variance, and skewness of the scores."""
    mean = np.mean(scores)
    variance = np.var(scores)
    skewness = skew(scores)
    return mean, variance, skewness

def plot_distribution(scores, title):
    """Plots histogram and density plot of the scores."""
    plt.figure(figsize=(10, 6))
    
    # Histogram with KDE
    sns.histplot(scores, bins=10, kde=True, stat="density", color='blue', alpha=0.5)
    
    # Add titles and labels
    plt.title(title)
    plt.xlabel('Scores')
    plt.ylabel('Density')
    
    # Show plot
    plt.grid()
    plt.show()

def letter_grades_absolute(score, thresholds):
    """Assigns a letter grade based on absolute score thresholds."""
    for grade, threshold in thresholds.items():
        if score >= threshold:
            return grade
    return 'F'  # Default to F if no thresholds are met

def letter_grades_relative(score, distribution):
    """Assigns a letter grade based on relative distribution."""
    if score >= distribution['A']:
        return 'A'
    elif score >= distribution['B']:
        return 'B'
    elif score >= distribution['C']:
        return 'C'
    elif score >= distribution['D']:
        return 'D'
    else:
        return 'F'

def z_score_scaling(scores):
    """Applies z-score scaling to the scores."""
    mean = np.mean(scores)
    std_dev = np.std(scores)
    return [(score - mean) / std_dev for score in scores]

def percentile_scaling(scores):
    """Applies percentile scaling to the scores."""
    return rankdata(scores) / len(scores)

def process_grades(filename, grading_method, parameters):
    """Reads student grades from a CSV file and calculates total and letter grades."""
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file)
            
            scores = []  # List to store total scores
            grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}  # Count of each grade
            if os.name == 'nt':
               os.system('cls')  # Clear the screen for Windows
            print(f"{'\t\tStudent Name':<25}{'\t\tExam1':<10}{'\t\tExam2':<10}{'\t\tExam3':<10}{'\t\tTotal':<10}{'\t\tGrade':<10}")
            print("=" * 183)    
            
            for row in csv_reader:
                first_name = row[0]
                last_name = row[1]
                exam1 = float(row[2])
                exam2 = float(row[3])
                exam3 = float(row[4])
                
                # Calculate total score as an average
                total_score = (exam1 + exam2 + exam3) / 3  
                scores.append(total_score)  # Collect scores
                
                # Determine grade based on selected method
                if grading_method == 'absolute':
                    grade = letter_grades_absolute(total_score, parameters)
                    grade_counts[grade] += 1  # Increment count for the assigned grade
                else:
                    scaled_score = z_score_scaling([total_score])[0]
                    grade = letter_grades_relative(total_score, parameters)
                
                
                # Print formatted output
                print(f"\t\t{first_name + ' ' + last_name:<25}\t{exam1:<10}\t\t{exam2:<10}\t\t{exam3:<10}\t\t{total_score:<10.2f}\t\t{grade:<10}")
                
            # Calculate and display statistics if relative grading is selected
            if grading_method == 'relative':
                mean, variance, skewness = calculate_statistics(scores)
                print("\nDescriptive Statistics:")
                print(f"Mean: {mean:.2f}")
                print(f"Variance: {variance:.2f}")
                print(f"Skewness: {skewness:.2f}")

                # Plotting the distribution before adjustments
                plot_distribution(scores, "Grade Distribution Before Adjustments")

                # Example adjustment (scaling by a factor)
                adjusted_scores = [score * 1.05 for score in scores]  
                
                # Plotting the distribution after adjustments
                plot_distribution(adjusted_scores, "Grade Distribution After Adjustments")
            else:
                # Summary statistics for absolute grading
                total_students = len(scores)
                print("\nSummary Statistics for Absolute Grading:")
                for grade in grade_counts:
                    percentage = (grade_counts[grade] / total_students) * 100 if total_students > 0 else 0
                    print(f"Percentage of {grade}: {percentage:.2f}%")    
            
            # Relative grading logic
            if grading_method == 'relative':
                # Apply z-score scaling for relative grading
                z_scores = z_score_scaling(scores)

                # Determine final grades based on specified distributions
                num_students = len(z_scores)
                
                # Create bins according to specified percentages
                thresholds = {
                    'A': int(num_students * parameters['A']),
                    'B': int(num_students * parameters['B']),
                    'C': int(num_students * parameters['C']),
                    'D': int(num_students * parameters['D'])
                }

                # Assign grades based on calculated bins
                final_grades = []
                
                sorted_z_scores = sorted(z_scores)

                for i in range(num_students):
                    if i < thresholds['A']:
                        final_grades.append('A')
                    elif i < thresholds['A'] + thresholds['B']:
                        final_grades.append('B')
                    elif i < thresholds['A'] + thresholds['B'] + thresholds['C']:
                        final_grades.append('C')
                    elif i < thresholds['A'] + thresholds['B'] + thresholds['C'] + thresholds['D']:
                        final_grades.append('D')
                    else:
                        final_grades.append('F')

                # Count final grades and print summary
                final_grade_counts = {grade: final_grades.count(grade) for grade in ['A', 'B', 'C', 'D', 'F']}
                
                print("\nFinal Grade Distribution Based on Relative Grading:")
                for grade in final_grade_counts:
                    percentage = (final_grade_counts[grade] / num_students) * 100 if num_students > 0 else 0
                    print(f"Percentage of {grade}: {percentage:.2f}%")

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if os.name == 'nt':
     os.system('cls')
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t\t\tGhulam Ishaq Khan Institue OF Engineering Sciences And Technology")
    print("\t\t\t\t\t\t\t\tThis Project IS Copyright Protected Act 1962")
    print("\t\t\t\t\t\t\t\t\t\tGrading Portal")
    time.sleep(5)
    if os.name == 'nt':
     os.system('cls')
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institute OF Engineering Sciences")
    print("\t\t\t\t\t\t\tBelow You have To Enter The Path To The CSV File Which Contains The Student Details")
    print("\t\t\t\t\t\t\tWe Have A Record For 83 Students Total")
    print("\t\t\t\t\t\t\tEach Record Will Have First Name Last Name And Marks For 3 Exams")
    filename = input("\t\t\t\t\t\t\tEnter the path to the CSV file: ")
    time.sleep(5)
    if os.name == 'nt':
     os.system('cls')
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    # Select grading method
    print("\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institute OF Engineering Sciences")
    print("\t\t\t\t\t\tSelect grading method:")
    print("\t\t\t\t\t\t1. Absolute Grading")
    print("\t\t\t\t\t\t2. Relative Grading")
    choice = int(input("\t\t\t\t\t\tEnter choice (1 or 2): "))
    time.sleep(3)
    if os.name == 'nt':
     os.system('cls')
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    while choice != 1 and choice != 2:
        print("\t\t\t\t\t\t\tPlease Enter Correct Choice")
        print("\t\t\t\t\t\t\t1. Absolute Grading")
        print("\t\t\t\t\t\t\t2. Relative Grading")
        choice = input("\t\t\t\t\t\tEnter choice (1 or 2)")
    # If the instructor selects Absolute    
    if choice == 1:
        if os.name == 'nt':
          os.system('cls')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institute OF Engineering Sciences")
        print("\t\t\t\t\t\tYou have chosen Absolute Grading. Now you need to define the grade thresholds.")
        thresholds = {
            # The get_float_input function will validate weather the user input is a float or not
            'A': get_float_input("\t\t\t\t\t\tEnter threshold for A (e.g., 90): "),
            'B': get_float_input("\t\t\t\t\t\tEnter threshold for B (e.g., 80): "),
            'C': get_float_input("\t\t\t\t\t\tEnter threshold for C (e.g., 70): "),
            'D': get_float_input("\t\t\t\t\t\tEnter threshold for D (e.g., 60): ")
        }
        process_grades(filename, 'absolute', thresholds)
    
    # If the instructor selects Relative
    elif choice == 2:
        if os.name == 'nt':
          os.system('cls')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("\t\t\t\t\t\tGrading Portal OF Ghulam Ishaq Khan Institute OF Engineering Sciences")
        print("\t\t\t\t\t\tYou have chosen Relative Grading. Now you need to specify the desired grade distribution.")
        distribution = get_distribution_input()
        process_grades(filename, 'relative', distribution)

if __name__ == "__main__":
    main()