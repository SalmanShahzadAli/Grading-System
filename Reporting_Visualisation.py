def generate_grade_report(data, thresholds, grading_policy, exam1_scores, exam2_scores, exam3_scores):
    """
    Generate a detailed report of original and adjusted grades.

    Parameters:
    - data: DataFrame containing student names and scores.
    - thresholds: Dictionary containing grade thresholds (for absolute grading).
    - grading_policy: Indicates whether the grading is relative or absolute.
    - exam1_scores: Scores for Exam 1.
    - exam2_scores: Scores for Exam 2.
    - exam3_scores: Scores for Exam 3.

    Returns:
    - A DataFrame containing original scores, assigned grades, and adjusted grades.
    """
    # Initialize adjusted scores
    exam1_adjusted = exam1_scores.copy()
    exam2_adjusted = exam2_scores.copy()
    exam3_adjusted = exam3_scores.copy()

    # Relative grading using z-score scaling
    if grading_policy == 1:  # Relative grading
        # Calculate z-scores for each exam
        z_scores_exam1 = calculate_z_scores(exam1_scores)
        z_scores_exam2 = calculate_z_scores(exam2_scores)
        z_scores_exam3 = calculate_z_scores(exam3_scores)

        # Adjust z-scores to a target scale (e.g., scale to a mean of 75)
        exam1_adjusted = z_scores_exam1 * 10 + 75  # Scale to a target mean
        exam2_adjusted = z_scores_exam2 * 10 + 75
        exam3_adjusted = z_scores_exam3 * 10 + 75

        # Assign grades based on original scores
        exam1_grades = Assign_Grades(exam1_scores, thresholds)
        exam2_grades = Assign_Grades(exam2_scores, thresholds)
        exam3_grades = Assign_Grades(exam3_scores, thresholds)

        # Create a report DataFrame
        report = pd.DataFrame({
            'Name': data.iloc[:, 0],
            'Exam 1 Score': exam1_scores,
            'Exam 1 Grade': [k for k, v in exam1_grades.items() for _ in range(v)],
            'Exam 1 Adjusted Score (Z-Score)': exam1_adjusted,
            'Exam 2 Score': exam2_scores,
            'Exam 2 Grade': [k for k, v in exam2_grades.items() for _ in range(v)],
            'Exam 2 Adjusted Score (Z-Score)': exam2_adjusted,
            'Exam 3 Score': exam3_scores,
            'Exam 3 Grade': [k for k, v in exam3_grades.items() for _ in range(v)],
            'Exam 3 Adjusted Score (Z-Score)': exam3_adjusted,
        })

    return report

# Generate the grade report
report = generate_grade_report(data, thresholds, grading_policy_number, exam1_scores, exam2_scores, exam3_scores)

# Display or save the report
print(report)  # You can also save it to a file if needed