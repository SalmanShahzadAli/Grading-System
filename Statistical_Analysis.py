# This Module will cover all of the statistics in the portal
# For relative grading, calculate descriptive statistics (mean, variance, skewness) for the input grades

import numpy as np
from scipy.stats import skew

def Calculate_Statistics_Relative_Grades(grades):
    # Calculate the mean of the grades
    mean = np.mean(grades)
    varaince = np.var(grades)
    skewness = skew(grades)
    return mean,varaince,skewness
    