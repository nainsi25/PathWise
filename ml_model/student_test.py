import pandas as pd
import os

# Load JEE Dataset
file_path = os.path.join("dataset", "jee_questions_cleaned.csv")

df = pd.read_csv(file_path)

print("JEE Dataset Loaded Successfully!")

# Display total questions
print("Total Questions:", len(df))

# Display subject-wise questions
print("\nSubject-wise Questions:")
print(df["subject"].value_counts())

# Display first 5 questions
print("\nSample Questions:")
for index, row in df.head().iterrows():
    print("\nQuestion:", row["question"])
    print("Subject:", row["subject"])
    print("Options:", row["options"])