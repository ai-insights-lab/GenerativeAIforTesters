import pandas as pd
from faker import Faker
import random

# Sample data provided
sample_data = """1, 45, Male, 150, 130/80, 200, Yes
2, 60, Female, 180, 140/90, 240, Yes
3, 35, Male, 120, 120/75, 180, No
4, 52, Female, 160, 135/85, 220, Yes
5, 48, Male, 155, 128/82, 210, Yes
6, 42, Female, 140, 125/78, 190, No
7, 55, Male, 170, 138/88, 230, Yes
8, 39, Female, 130, 118/76, 175, No
9, 58, Male, 165, 142/92, 235, Yes
10, 50, Female, 175, 130/85, 250, Yes"""

# Splitting sample data into rows and columns
rows = [row.split(', ') for row in sample_data.split('\n')]
columns = ['Patient_ID', 'Age', 'Gender', 'Blood_Sugar_Level', 'Blood_Pressure', 'Cholesterol_Level', 'Diabetic']

# Load sample data into a DataFrame
df = pd.DataFrame(rows, columns=columns)

# Initialize Faker
faker = Faker()

# Generate synthetic data
synthetic_data = []
for index, row in df.iterrows():
    synthetic_row = {
        'Patient_ID': index + 1,
        'Age': random.randint(int(row['Age']) - 5, int(row['Age']) + 5),
        'Gender': row['Gender'],  # Keep gender the same
        'Blood_Sugar_Level': random.randint(int(row['Blood_Sugar_Level']) - 10, int(row['Blood_Sugar_Level']) + 10),
        'Blood_Pressure': f"{random.randint(110, 150)}/{random.randint(70, 90)}",  # Generate random blood pressure
        'Cholesterol_Level': random.randint(int(row['Cholesterol_Level']) - 20, int(row['Cholesterol_Level']) + 20),
        'Diabetic': row['Diabetic']  # Keep diabetic status the same
    }
    synthetic_data.append(synthetic_row)

# Convert list of dictionaries to DataFrame
synthetic_df = pd.DataFrame(synthetic_data)

# Print synthetic data
print("Synthetic Data:")
print(synthetic_df)

# Save synthetic data to CSV
synthetic_df.to_csv("D:/GenAI_Workshop/synthetic_data_new.csv", index=False)