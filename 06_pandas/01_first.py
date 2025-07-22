import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
calories = {"day1": 420, "day2": 380, "day3": 390}
a = [1,7,2,4,5]
# my_var = pd.Series(calories)

my_var = pd.DataFrame(mydataset)

print(my_var)
print()
print(my_var.loc[[0,1]])