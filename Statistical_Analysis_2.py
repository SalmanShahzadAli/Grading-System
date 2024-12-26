# Plot histograms or density plots of the grade distribution before and after adjustments
# we are going to import two libraries for ploting histograms and density plots

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

# Now, let's plot the histograms and density plots for each exam score
plt.figure(figsize=(15, 5))

# Plot for Exam Score 1
plt.subplot(1, 3, 1)
sns.histplot(exam1_scores, bins=10, kde=True, color='blue')
plt.title('Distribution of Exam Score 1')
plt.xlabel('Scores')
plt.ylabel('Frequency')

# Plot for Exam Score 2
plt.subplot(1, 3, 2)
sns.histplot(exam2_scores, bins=10, kde=True, color='green')
plt.title('Distribution of Exam Score 2')
plt.xlabel('Scores')
plt.ylabel('Frequency')

# Plot for Exam Score 3
plt.subplot(1, 3, 3)
sns.histplot(exam3_scores, bins=10, kde=True, color='orange')
plt.title('Distribution of Exam Score 3')
plt.xlabel('Scores')
plt.ylabel('Frequency')

# Show the plots
plt.tight_layout()
plt.show()


# The below Code is For Relative Grading
def plot_grade_distributions(original_scores, adjusted_scores, exam_name):
    """Plot histograms and density plots for original and adjusted scores."""
    plt.figure(figsize=(12, 6))

    # Original Scores
    plt.subplot(1, 2, 1)
    sns.histplot(original_scores, bins=10, kde=True, color='blue', stat='density')
    plt.title(f'Distribution of {exam_name} Scores (Original)')
    plt.xlabel('Scores')
    plt.ylabel('Density')

    # Adjusted Scores
    plt.subplot(1, 2, 2)
    sns.histplot(adjusted_scores, bins=10, kde=True, color='orange', stat='density')
    plt.title(f'Distribution of {exam_name} Scores (Adjusted)')
    plt.xlabel('Scores')
    plt.ylabel('Density')

    plt.tight_layout()
    plt.show()