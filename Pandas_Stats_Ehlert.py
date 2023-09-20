"""
Program Name: Pandas_Stats_Ehlert.py
Author: Tony Ehlert
Date: 9/13/2023

Program Description: The program reads a .csv file into a Pandas dataframe and uses the Pandas library to perform
some statistical analysis on the dataframe.
"""
import pandas as pd

### Load data into Pandas dataframe using read_csv (Please have the csv file in the same directory as your program)
ign_df = pd.read_csv("ign.csv")
# print(ign_dataframe)
# print()

### Print the shape of the dataframe
print(f"Shape of ign_dataframe: {ign_df.shape}")
print()

### Remove the "Unnamed" column using iloc (or drop)
ign_unnamed_dropped_df = ign_df.drop(["Unnamed: 0"], axis=1)
# print(ign_unnamed_dropped_dataframe)

### Print the title, genre and release year columns using .loc
print("PRINT OF \"title\", \"genre\", and \"release_year\" columns using .loc: ")
print(ign_unnamed_dropped_df.loc[:, ["title", "genre", "release_year"]])
print()

### Print the mean, max, and standard deviation for the scores of the dataframe ("score" column)
print(f"The mean of the \"score\" column is: {ign_unnamed_dropped_df['score'].mean()}")
print(f"The max of the \"score\" column is: {ign_unnamed_dropped_df['score'].max()}")
print(f"The standard deviation of the \"score\" column is: {ign_unnamed_dropped_df['score'].std()}")
print()

### Convert the scores column to 100 base by multiplying it by 10
ign_score_base_100_df = ign_unnamed_dropped_df.copy()
ign_score_base_100_df["score"] = ign_score_base_100_df["score"] * 10
# print(f"ign_score_base_100_df \"score\" column @ base 100: ")
# print(ign_score_base_100_df["score"])

### Create a new df that only includes rows with score above the mean score of the main df (should have 11,373 rows)

# create a dataframe of boolean values based on score greater than mean
score_abv_mean_bool_df = ign_score_base_100_df["score"] > ign_score_base_100_df["score"].mean()
# print(score_abv_mean_bool_df)

# create dataframe of only scores above mean value by using ign_score_base_100_df & score_abv_mean_bool_df
ign_score_abv_mean_df = ign_score_base_100_df[score_abv_mean_bool_df]
# print(ign_score_abv_mean_df)

### Print series that lists count of scores by platform from above mean df sorted desc (PC should have 2191 for count)
print(ign_score_abv_mean_df["platform"].value_counts().sort_values(ascending=False))
