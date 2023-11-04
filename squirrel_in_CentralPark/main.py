import pandas as pd

fur_name = "Primary Fur Color"
squirrel_ok = []
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231104.csv")
gray_squirrel_cnt = len(data[data[fur_name] == "Gray"])
squirrel_ok.append(gray_squirrel_cnt)
red_squirrel_cnt = len(data[data[fur_name] == "Cinnamon"])
squirrel_ok.append(red_squirrel_cnt)
black_squirrel_cnt = len(data[data[fur_name] == "Black"])
squirrel_ok.append(black_squirrel_cnt)

squirrel_dict = {
    "Fur": ("Gray", "Red", "Black"),
    "Counter": squirrel_ok
}
squirrel_df = pd.DataFrame(squirrel_dict)
squirrel_df.to_csv("final_squirrel.csv")
print(squirrel_df)
