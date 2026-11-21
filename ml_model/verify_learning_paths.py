import pandas as pd

data = pd.read_csv("learning_path_data.csv")

print("COMPLETE LEARNING PATH DATASET VERIFICATION\n")

print("Total Records:", len(data))

print("\nTotal Goals:", data["goal"].nunique())

print("\nGoal-wise Sub-goals:")

for goal in sorted(data["goal"].unique()):

    goal_data = data[data["goal"] == goal]

    print("\nGoal:", goal)
    print("Sub-goals:", goal_data["sub_goal"].nunique())

    for sub_goal in sorted(goal_data["sub_goal"].unique()):

        path = goal_data[
            goal_data["sub_goal"] == sub_goal
        ]

        topic_count = path["topic"].nunique()

        if topic_count == 15 and len(path) == 15:
            print("PASS:", sub_goal, "-", topic_count, "topics")
        else:
            print("CHECK:", sub_goal)
            print("Total rows:", len(path))
            print("Unique topics:", topic_count)

        if path["sequence"].duplicated().any():
            print("WARNING: Duplicate sequence in", sub_goal)

print("\nLevel-wise Records:")
print(data["level"].value_counts())

print("\nVerification Completed!")