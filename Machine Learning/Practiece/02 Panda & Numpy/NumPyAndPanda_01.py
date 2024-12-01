#!/usr/bin/env python
# coding: utf-8


# Importing required libraries
import numpy as np
import pandas as pd

# Step 1: Create synthetic data using NumPy
np.random.seed(42)  # Setting a seed ensures reproducibility; results will always be the same.

# Defining names of students and subjects
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']  # List of student names
subjects = ['Math', 'Science', 'English', 'Bangla']  # List of subjects

# Generating random scores for students in each subject
# Scores will be integers between 50 and 100 for a 5x4 matrix (5 students, 4 subjects)
scores = np.random.randint(50, 100, size=(5, 4))

# Displaying the generated data
print('Names:', names)
print('Subjects:', subjects)
print('Scores (raw data):\n', scores)



# Step 2: Create a DataFrame with Pandas
# Create a DataFrame where rows represent students and columns represent subjects
df = pd.DataFrame(scores, index=names, columns=subjects)
print("\nInitial DataFrame:\n", df)



# Step 3: Calculate statistics
# Calculate the average score for each student
# axis=1 means the operation (mean) is performed across columns (i.e., per row/student)
average_scores = df.mean(axis=1)

# Add a new column 'Average' to the DataFrame to store the average scores
df['Average'] = average_scores
print("\nDataFrame with Average Scores:\n", df)



# Step 4: Identify top performers
# Find the name of the student with the highest average score
# idxmax() returns the index (student name) of the maximum value in the 'Average' column
top_performer = df['Average'].idxmax()
print("\nTop Performer:", top_performer)



# Step 5: Normalize scores
# Normalization rescales data to a range of 0 to 1
# Formula: normalized_value = (value - min_value) / (max_value - min_value)
normalized_scores = (scores - scores.min()) / (scores.max() - scores.min())

# Create a new DataFrame to store normalized scores, keeping the same structure as the original
df_normalized = pd.DataFrame(normalized_scores, index=names, columns=subjects)
print("\nNormalized DataFrame (scores scaled to 0-1):\n", df_normalized)



# Step 6: Save processed data to a CSV file
# Save the DataFrame (including averages) to a CSV file
# df.to_csv('student_scores.csv', index=True)  # index=True includes the student names
# print("\nProcessed data saved to 'student_scores.csv'.")

# Advanced Step: Transpose DataFrame (swap rows and columns)
# Transpose the DataFrame so that subjects become the index and students become the columns
df_transposed = pd.DataFrame(scores.T, index=subjects, columns=names)
print("\nDataFrame with Subjects as Index:\n", df_transposed)



# Accessing specific data in the transposed DataFrame
# Example 1: Get all scores for Bob (a single column from the transposed DataFrame)
print("\nScores for Bob:\n", df.loc['Bob'])



# Example 2: Get all students' scores in Math (a single row from the transposed DataFrame)
print("\nScores in Math:\n", df['Math'])



# Adding new statistics: Average score per subject
# axis=1 calculates averages for each subject (across students in this layout)
df_transposed['Subject Average'] = df_transposed.mean(axis=1)
print("\nDataFrame with Subject Averages:\n", df_transposed)



# Advanced Example: Conditional Filtering, Grouping, and Custom Functions
# Advanced 2.1: Conditional filtering
# Find all students who scored above 80 in Science
high_scorers_science = df[df['Science'] > 80]
print("\nStudents scoring above 80 in Science:\n", high_scorers_science)



# Advanced 2.2: Adding a performance
# Define a function to categorize students based on their average score
def performance(avg):
    if avg >= 85:
        return 'Outstanding'
    elif avg >= 70:
        return 'Good'
    else:
        return 'Needs Improvement'

# Apply the function to the 'Average' column and create a new column
df['Performance'] = df['Average'].apply(performance)
print("\nDataFrame with Performance Categories:\n", df)



# Advanced 2.3: Grouping and aggregation
# Group by performance category and calculate statistics for each group
performance_summary = df.groupby('Performance').agg(
    Average_Score=('Average', 'mean'),
    Max_Score=('Average', 'max'),
    Min_Score=('Average', 'min'),
    Count=('Average', 'count')
)
print("\nPerformance Summary by Category:\n", performance_summary)



# Advanced 2.4: Identify the student with the highest score in each subject
top_in_each_subject = df[subjects].idxmax()
print("\nTop Student in Each Subject:\n", top_in_each_subject)

