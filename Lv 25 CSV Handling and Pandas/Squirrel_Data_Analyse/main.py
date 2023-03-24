import pandas
SOURCE_FILE = "Lv 25 CSV Handling and Pandas/Squirrel_Data_Analyse/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
TARGET = "Lv 25 CSV Handling and Pandas/Squirrel_Data_Analyse/fur_color_counts.csv"

squirrel_data = pandas.read_csv(SOURCE_FILE)
color_counts = squirrel_data.value_counts("Primary Fur Color").rename_axis("Fur Color").reset_index(name="Count")

new_data = pandas.DataFrame(data = color_counts)
new_data.to_csv(TARGET)