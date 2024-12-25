# Relative grading: Apply relative grading algorithms (e.g., curve fitting to normal distribution, z-score 
# scaling, or percentile-based scaling).

# The Below Function will handle calculation of Z-Scores
def calculate_z_scores(scores):
    mean = scores.mean()
    std_dev = scores.std()
    z_scores = (scores - mean) / std_dev
    return z_scores

# Calculate z-scores for each exam
z_scores_exam1 = calculate_z_scores(exam1_scores)
z_scores_exam2 = calculate_z_scores(exam2_scores)
z_scores_exam3 = calculate_z_scores(exam3_scores)

# Display the z-scores
    print("\n\t\t\t\t\tZ-Scores for Exam 1:")
    for name, score, z_score in zip(data['First Name'], exam1_scores, z_scores_exam1):
        print(f"\t\t\t\t\t{name} {score} -> Z-Score: {z_score:.2f}")

    print("\n\t\t\t\t\tZ-Scores for Exam 2:")
    for name, score, z_score in zip(data['First Name'], exam2_scores, z_scores_exam2):
        print(f"\t\t\t\t\t{name} {score} -> Z-Score: {z_score:.2f}")

    print("\n\t\t\t\t\tZ-Scores for Exam 3:")
    for name, score, z_score in zip(data['First Name'], exam3_scores, z_scores_exam3):
        print(f"\t\t\t\t\t{name} {score} -> Z-Score: {z_score:.2f}")
