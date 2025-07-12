#import library 
import pandas as pd
# Read File
df = pd.read_csv("student.csv")
# Show First five rows
print(df.head())
# Show Total number of rows and column in data
print(df.shape)
# Show Average of marks
print(df["marks"].mean())
# Filter by high marks
print(df[df["marks"] > 80])
# Prints Maximum marks
print(df["marks"].max())

# Filter highscorers to save into another file 
high_scorers = df[df["marks"] > 80]
# Create and save  highscorers data to file 
high_scorers.to_csv("high_scorers.csv",index=False)
# Print Succesfully
print("High scorers saved succesfully ")
print(high_scorers)