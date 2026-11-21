import pandas as pd
import json
import os

# Dataset file path
file_path = os.path.join(
    "dataset",
    "JEE-Main-2025-Question-Paper-with-Solution-22th-Jan-2025-Shift-2-PDF.json"
)

# Read JSON file
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print("Dataset loaded successfully!")

# Convert JSON data into DataFrame
df = pd.DataFrame(data)

# Total questions
print("\nTotal Questions:", len(df))

# Dataset columns
print("\nDataset Columns:")
print(df.columns.tolist())

# Subject-wise question count
print("\nSubject-wise Questions:")
print(df["subject"].value_counts())

# First 5 questions
print("\nFirst 5 Questions:")
print(df[["question_number", "subject"]].head())
# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate questions
print("\nDuplicate Questions:")
print(df.duplicated(subset=["question"]).sum())
# Display questions with missing answers
missing_answers = df[df["answer"].isnull()]

print("\nQuestions with Missing Answers:")
print(missing_answers[["question_number", "subject"]])
# Remove rows with missing answers
df_cleaned = df.dropna(subset=["answer"]).copy()

print("\nDataset Cleaning Completed!")
print("Original Questions:", len(df))
print("Cleaned Questions:", len(df_cleaned))
print("Removed Questions:", len(df) - len(df_cleaned))

# Subject-wise count after cleaning
print("\nCleaned Subject-wise Questions:")
print(df_cleaned["subject"].value_counts())
# Save cleaned dataset
output_path = os.path.join("dataset", "jee_questions_cleaned.csv")

df_cleaned.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("File location:", output_path)