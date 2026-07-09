import pandas as pd

# Load dataset
df = pd.read_csv("Dataset.csv")

# Average rating by cuisine
print("\nAverage Rating by Cuisine:")
print(df.groupby("Cuisines")["Aggregate rating"].mean().sort_values(ascending=False).head(10))

# Most popular cuisines based on votes
print("\nTop 10 Most Popular Cuisines (by Votes):")
print(df.groupby("Cuisines")["Votes"].sum().sort_values(ascending=False).head(10))

# Number of restaurants for each cuisine
print("\nTop 10 Cuisines by Restaurant Count:")
print(df["Cuisines"].value_counts().head(10))