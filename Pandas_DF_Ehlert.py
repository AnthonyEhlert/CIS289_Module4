"""
Program Name: Pandas_DF_Ehlert.py
Author: Tony Ehlert
Date: 9/13/2023

Program Description: This program loads data into a Pandas dataframe and then uses the Pandas library to look at
specific statistics of the data loaded as well as manipulate the dataframe.
"""
import pandas as pd

# load initial data into Pandas dataframe
first_dataframe = pd.DataFrame(
    {
        "Day of week" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Max Temp" : [47, 44, 33, 34, 30, 29, 45],
        "Min Temp" : [36, 30, 27, 30, 16, 12, 24]
    }
)

# print the statistical data about this frame (mean, standard dev, min, max)
print(f"Statistical data from Pandas.describe():\n{first_dataframe.describe()}\n")
print(f"Mean of numerical values:\n{first_dataframe.mean(numeric_only=True)}\n")
print(f"Standard deviation of numerical values:\n{first_dataframe.std(numeric_only=True)}\n")
print(f"Min value of numerical values:\n{first_dataframe.min(numeric_only=True)}\n")
print(f"Max value of numerical values:\n{first_dataframe.max(numeric_only=True)}\n")

# create another dataframe
second_dataframe = pd.DataFrame(
    {
        "Day of week" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Precip" : [0.21, .01, 0, .01, 0.01, 0, 0],
        "New Snow" : [0, 0, 0, 0.1, 0.3, 0, 0]
    }
)

# Merge the two dataframes on the "Day of week" common identifier and print the new dataframe to the console
merged_dataframe = first_dataframe.merge(second_dataframe, how= "left", on= ["Day of week"])
# print(merged_dataframe)
# print()

# Set the index of the new dataframe to be on the "Day of week" column
day_of_wk_index_dataframe = merged_dataframe.set_index("Day of week")
# print(day_of_wk_index_dataframe)
# print()

# Convert the "Max Temp" and "Min Temp" columns to Celcius ((F -32)*5/9)
celsius_dataframe = day_of_wk_index_dataframe.copy()
celsius_dataframe["Max Temp"] = (celsius_dataframe["Max Temp"] - 32) * 5/9
celsius_dataframe["Min Temp"] = (celsius_dataframe["Min Temp"] - 32) * 5/9
# print(celsius_dataframe)
# print(day_of_wk_index_dataframe)
# print()

# Add an "Ave Temp" column which is the average of "Max Temp" and "Min Temp"
ave_temp_dataframe = celsius_dataframe.copy()
ave_temp_dataframe.insert(4, "Ave Temp", (ave_temp_dataframe["Max Temp"] + ave_temp_dataframe["Min Temp"]) / 2)
# print(ave_temp_dataframe)
# print()

# Reindex the dataframe so the "Ave Temp" column is right after the "Min Temp" column
final_dataframe = ave_temp_dataframe.reindex(columns=["Max Temp", "Min Temp", "Ave Temp", "Precip", "New Snow"])

# Print the dataframe to the screen
print(final_dataframe)
