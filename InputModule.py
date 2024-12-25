# This is the Input Module In Which The User Will Select Between
# Relative And Absolute
# We Are Giving The User And Option To Select Between Either He
# Wants To Input Data From a csv file or Excel Sheet.

# The below libraries Are Included To Bring The Necessary Things.
import pandas as pd

def input_grades():
    """Allow the user to choose the file type and load grades accordingly."""
    try:
        # Prompt user for file type
        file_type = input("Enter the file type (CSV/Excel): ").strip().lower()
        if file_type not in ["csv", "excel"]:
            raise ValueError("Invalid file type. Please enter 'CSV' or 'Excel'.")

        # Prompt user for file path
        file_path = input("Enter the path to the file: ").strip()

        # Load file based on type
        if file_type == 'csv':
            data = pd.read_csv(file_path)
        elif file_type == 'excel':
            data = pd.read_excel(file_path)

        print()
        print("Fetching Data From",file_type.upper(),"Sheet")
        # Validate required columns
        if len(data.columns) < 5:
            raise ValueError("The file must contain at least 5 columns: FirstName, LastName, and three exam scores.")

        # Define the sections explicitly
        sections = {
            "First Name": data.iloc[:, 0],  # First column
            "Last Name": data.iloc[:, 1],  # Second column
            "Exam 1": data.iloc[:, 2],     # Third column
            "Exam 2": data.iloc[:, 3],     # Fourth column
            "Exam 3": data.iloc[:, 4]      # Fifth column
        }

        # Combine sections into a structured DataFrame
        structured_preview = pd.DataFrame(sections)

        # Display a structured preview
        print("\nFile loaded successfully! Here's a structured preview of the data:")
        print(structured_preview.head().to_string(index=False))

        return data
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        return None
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    input_grades()


