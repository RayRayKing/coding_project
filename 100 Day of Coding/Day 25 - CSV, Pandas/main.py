import pandas
# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
#
# series_temp = data["temp"]
#
#
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print((monday.temp * 1.8) + 32)
# print(series_temp.describe())

# Count & Build dataframe for count of unique fur color

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_list = data["Primary Fur Color"].unique().tolist()
color_list.pop(0)
data_df = {}
data_df["fur_color"] = []
data_df["count"] = []
for color in color_list:
    data_df["fur_color"].append(color)
    data_df["count"].append(len(data[data["Primary Fur Color"] == color]))
    # num = data["Primary Fur Color" == color]
    # print(num)'.,

print(data_df)
new_df = pandas.DataFrame(data_df)
print(new_df)
