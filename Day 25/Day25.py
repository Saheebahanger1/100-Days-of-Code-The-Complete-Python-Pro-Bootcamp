with open("/Users/khalidz/Desktop/Saheeb Ahanger/Day 25/weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())

print(data["temp"].max())

print(data["temp"].min())

print(data["temp"].median())

print(data["temp"].mode())

print(data["temp"].std())

print(data["temp"].var())

print(data["temp"].quantile())

# Get Data in Columns.
print(data['condition'])
print(data.condition)

# Get Data in Rows.
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# print(monday.condition)
print(monday.temp)
fahrenheit = (monday.temp * 1.8) + 32
print(fahrenheit)


# Create a Dataframe from scratch
data_dict ={
    "students": ["Saheeb", "Khalid", "Angela"],
    "scores": [80, 85, 99]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")

import pandas as pd 
data = pd.read_csv("Dataset.csv")

grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
print(grey_squirrel)

grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")