# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column_index = int(position[0])-1
row_index = int(position[1])-1

if row_index == 0:
  row1[column_index] = "X"
elif row_index ==1:
  row2[column_index] = "X"
elif row_index == 2:
  row3[column_index] = "X"
else:
  print ('Wrong input data')


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")