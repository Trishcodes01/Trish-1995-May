# File I/O
# import csv
import xlwt
# save it as a book and a File.
from tempfile import TemporaryFile as TF

read_file = open("C:/Users/beatrice1/Desktop/python/Rawfile.txt", mode = "r", encoding = "utf-8")

# To have overview
whole_data = read_file.readlines()
# print(len(whole_data))
# print(whole_data[:5])

##To remove the unwanted '\n' from every entry in the data
refined_data = [entry.rstrip("\n") for entry in whole_data]
# print(refined_data[:5])

# Procedure for sorted
fel = [("High", 3), ("Low", 2), ("non", 6)]
new_output = sorted(fel, key = lambda a:a[1])
# print(new_output)

# Sort according to date:
# note strptime takes in two item and strftime remove two
# we used split to get iterable itemised out.
from datetime import datetime as dt
sorted_refined_data = sorted(refined_data, key = lambda a : dt.strptime(a.split(" on ")[1], "%d-%m-%Y"))
# print(sorted_refined_data[:5])
# note to get the last five numbers use:
# print(sorted_refined_data[-5])

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

# new_file = open("C:/Users/beatrice1/Desktop/python/raveurban.csv", mode = "w", encoding = "utf-8", newline = "")

# pen = csv.writer(new_file)
# pen.writerow(["name", "sales", "date"])

# for num in range(len(sorted_refined_data)):
#     pen.writerow([list_of_names[num], list_of_sales[num], list_of_dates[num]])

# list_of_names = set(list_of_names)
# print(len(list_of_names))

# new_file.close()

new = {}
for name, amount in zip(list_of_names, list_of_sales):
    new[name] = new.get(name, 0) + amount
# print(new)
# print(len(new))

sorted_new = dict(sorted(new.items(), key = lambda a : a[0]))
# print(sorted_new)

# How to get the list of names and sales from the Dict
# value means sales 
# FIRST EXCEL SHEET DATA
agent_names = list(sorted_new.keys())
agent_sales = list(sorted_new.values())
agent_commission = [amount * 0.055 for amount in agent_sales]
total_sales = sum(agent_sales)
agent_contribution = list(map(lambda a :str(round((a /total_sales) *100, 2)) + "%", agent_sales))

#  SECOND EXCEL SHEET DATA
total_commission = sum(agent_commission)
total_revenue = sum(agent_sales)
net_revenue = total_revenue - total_commission


# xlwt is a Module.
# GETTING THE BOOK
# NET INCOME INVOLVES ALL THE REVENUES
book = xlwt.Workbook()

# ADDING THE SHEETS
first_sheet = book.add_sheet("agents' records")
second_sheet = book.add_sheet("net income")

# WRITING INTO THE FIRST SHEET
# THE HEADER IN ROW AND COLUMNS
# FOR THE HEADER USE ENUMERATE
first_sheet.write(0, 0, "agent name")
first_sheet.write(0, 1, "agent sales")
first_sheet.write(0, 2, "agent commission")
first_sheet.write(0, 3, "agent contribution")


# column is constant, row changes
for index, entry in enumerate(agent_names):
    first_sheet.write(index + 1, 0, entry)

for index, entry in enumerate(agent_sales):
    first_sheet.write(index + 1, 1, entry)

for index, entry in enumerate(agent_commission):
    first_sheet.write(index + 1, 2, entry)

for index, entry in enumerate(agent_contribution):
    first_sheet.write(index + 1, 3, entry)


# WRITING INTO THE SECOND SHEET
second_sheet.write(0, 0, "total revenue")
second_sheet.write(0, 1, "total commission")
second_sheet.write(0, 2, "net revenue")

second_sheet.write(1, 0, total_revenue)

second_sheet.write(1, 1, total_commission)

second_sheet.write(1, 2, net_revenue)  

# Diff btw the csv file and Tf
book.save("C:/Users/beatrice1/Desktop/python/kalon.xls")  
book.save(TF())







