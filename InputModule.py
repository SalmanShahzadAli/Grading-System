# This is the Input Module In Which The User Will Select Between
# Relative And Absolute
# We Are Giving The User And Option To Select Between Either He
# Wants To Input Data From a csv file or Excel Sheet.

# The below libraries Are Included To Bring The Necessary Things.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def input_grades():
    """Allow the user to choose the file type and load grades accordingly."""
    try:
        file_type = input("Enter the file type (CSV/Excel): ").strip().lower()
        file_path = input("Enter the path to the file: ").strip()

        if file_type == 'csv':
            data = pd.read_csv(file_path)
        elif file_type == 'excel':
            data = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file type. Please choose 'CSV' or 'Excel'.")
        
        print("File loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def main():
    grades = input_grades()
