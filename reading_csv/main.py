import pandas
import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data)

# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# mean_temp = data["temp"].mean()
# print(mean_temp)
# max_temp = data["temp"].max()
# print(max_temp)
#
# Get data in Column
# # like a string
# print(data["condition"])
#  like a object
# print(data.condition)

# Get data in row
print(data[data.day == "Monday"])
print()
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# Convert Celsiusz to FarenHeit
# F = temp*1,8+32
temp_f = (monday.temp * 1.8) + 32
print(temp_f)

# Create DataFrame from scratch

data_dict = {
    "students": ["Artur", "Rafa", "Jan"],
    "scores": [76, 56, 64],
}
new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data.csv")