# For absolute grading, the system should still provide summary statistics (e.g., the percentage of students 
# falling into each grade category)
# As We have Already Extracted The Exam Score Hence We Dont need To Do That Again

def Assign_Grades(scores, thresholds):
    """
    Assign grades based on the defined thresholds.

    Parameters:
    - scores: A list or array of exam scores.
    - thresholds: A dictionary containing the grade thresholds.

    Returns:
    - A dictionary with the count of students in each grade category.
    """
    grade_counts = {grade: 0 for grade in thresholds.keys()}
    
    for score in scores:
        if score >= thresholds['A']:
            grade_counts['A'] += 1
        elif score >= thresholds['B']:
            grade_counts['B'] += 1
        elif score >= thresholds['C']:
            grade_counts['C'] += 1
        elif score >= thresholds['D']:
            grade_counts['D'] += 1
        else:
            grade_counts['F'] += 1

    return grade_counts

