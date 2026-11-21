import pandas as pd
from pathlib import Path

# Load learning path dataset
data = pd.read_csv(
    Path(__file__).resolve().parent / "learning_path_data.csv"
)

def generate_learning_path(goal, sub_goal, available_days, daily_hours):

    # Filter data according to selected goal and sub-goal
    path = data[
        (data["goal"].str.lower().str.strip() == goal.lower().strip()) &
        (data["sub_goal"].str.lower().str.strip() == sub_goal.lower().strip())
    ]

    print("Selected Goal:", goal)
    print("Selected Sub Goal:", sub_goal)

    if path.empty:
        return "No learning path found for these selections."

    # Calculate estimated study time
    total_days = path["estimated_days"].sum()
    total_hours = total_days * 2

    daily_hours = int(daily_hours)
    available_days = int(available_days)

    required_days = total_hours / daily_hours

    print("Total Estimated Study Hours:", total_hours)
    print("Available Days:", available_days)
    print("Required Days:", round(required_days, 1))

    # Check whether the goal is achievable
    if required_days <= available_days:
        print("Status: Your learning goal is achievable!")

    else:
        suggested_hours = total_hours / available_days

        print("Status: More study time is required.")
        print("Suggested Daily Study Hours:", round(suggested_hours, 1))

    # Display complete learning path in sequence
    result = path.sort_values("sequence").reset_index(drop=True)

    return result[["sequence", "topic", "priority", "estimated_days"]]

# Test the recommendation function
if __name__ == "__main__":

    learning_path = generate_learning_path(
        "devops",
        "linux",
        30,
        2
    )

    print("\nRecommended Learning Path:\n")
    print(learning_path)