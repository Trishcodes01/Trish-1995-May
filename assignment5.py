from datetime import datetime as dt
import csv
import xlwt
from tempfile import TemporaryFile as TF

read_file = open("C:/Users/beatrice1/Desktop/python/Rawfile.txt", mode = "r", encoding = "utf-8")
whole_data = read_file.readlines()

refined_data = [entry.rstrip("\n") for entry in whole_data]
sorted_refined_data = sorted(refined_data, key = lambda a : dt.strptime(a.split(" on ")[1], "%d-%m-%Y"))
# print(sorted_refined_data[:5])

list_of_names = []
list_of_sales = []
list_of_dates = []

for entry in sorted_refined_data:
    extracted_name = entry.split(" : ")[0]
    list_of_names.append(extracted_name)

    extracted_sales = int(entry.split(" ")[3].lstrip("₦"))
    list_of_sales.append(extracted_sales)

    extracted_date = entry.split(" ")[5].replace("-", "/")
    list_of_dates.append(extracted_date)
    # print(list_of_names)
    # break


new = {}
for name, amount in zip(list_of_names, list_of_sales):
    new[name] = new.get(name, 0) + amount
# print(new)
# print(len(new))

# A
pushing = dict(sorted(new.items(), key = lambda a : a[1], reverse = True))
outstanding = list(pushing)
print(pushing)
outstanding[ :10]
outstanding = [(key, value) for key, value in pushing.items()]
print(outstanding[ :10])

# B
rave = list(map(lambda a: str(a), list_of_dates))
print(rave)
print(len(rave))
crave = list(map(lambda r : r.split("/")[1], rave))
print(crave)
print(len(crave))
ave = list(map(lambda s: dt.strptime(s, "%m"), crave))
print(len(ave))
nave = list(map(lambda n:n.strftime("%B"), ave))
print(nave)
print(len(nave))
view = {}
for month, amount in zip(nave , list_of_sales):
    view[month] = view.get(month, 0) + amount
chills = [(key, values) for key, values in view.items()]
print(chills)

# 5C
month = sorted(chills, key = lambda a:a[1])
print(month)
low_month = month[0][0]
high_month = month[-1][0]
print(f"{low_month} is the month with the lowest sales and {high_month} is the month with the highest sales")



# 5D
sort_agent_names = dict(sorted(list_of_sales.items(), key = lambda a : a[0]))
print(sort_agent_names)
agent_names = list(sort_agent_names.keys())
agent_sales = list(sort_agent_names.values())
agent_commission = [amount*0.055 for amount in agent_sales]

dripped = {}
for names, commission in zip(agent_names, agent_commission):
    dripped[names] = dripped.get(names, 0) + commission
    print(dripped)
    print(len(dripped))


