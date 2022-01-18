# coverting list to str
# new_file = ["30", "33"]
# new = str(["30", "33"])
# print(new[1])

import time
# print("Beautiful")
# time.sleep(10)
# print("Girl")

# random shuffle
# import random as rd
# rd.seed(9)
# list_of_names = ['steve', 'dwayne','freya', 'nelson', 'sam', 'john', 'abu', 'binta']
# print(list_of_names)
# rd.shuffle(list_of_names)
# print("\n")
# print(list_of_names)

# random choice
# print(list_of_names)
# print("\n")
# random_pick = rd.choice(list_of_names)
# print(random_pick)

# random sample
# print(list_of_names)
# print("\n")
# multiple_picks = rd.sample(list_of_names, k = 3)
# print(multiple_picks)

# random randrange
# random_num = rd.randrange(9, 23, 3)
# print(random_num)

# random seed

# datetime
from datetime import datetime as dt

# current_dt = dt.now()
# print(current_dt)

# output = current_dt.year
# print(output)

# datetime.strftime
# output2 = current_dt.strftime("%A")
# print(output2)

# output3 = current_dt.strftime("%d")
# print(output3)

# output4 = current_dt.strftime("%B")
# print(output4)

# fake_date = "9/4/2021"
# real_date = dt.strftime(fake_date, "%d/%m/%Y")
# print(real_date)

notable_days = ["01/01/2021", "15/01/2021", "14/02/2021", "01/04/2021", "29/05/2021", "12/06/2021", "01/10/2021", "25/12/2021", "26/12/2021"]

# notable_map = map(lambda a: dt.strptime(a, "%d/%m/%Y"), notable_days)
# print(notable_days[0])
# print (list(notable_map))

# nott = notable_map[0]
# print(nott)

# new_string = "blue sky"
# print(new_string[2:8:2])

# conditional
# if conditional
# Block of code
# else:
# Block of code
# if 77 > 77:
#     print("Yes")
# else:
#     print("No")

# get_data = input("random: ")
# if len(get_data) == len(set(get_data)):
#     print("There are no duplicates")
# else:
#     print("There are diplicates")

# get_data = input("information: ")
# if int(get_data) % 2 == 0:
#     print("Even number")
# else:
#         print("odd number")

# elf if you are checking for multiple conditions with different block of codes
# get_data = input("Enter data here: ")
# if int(get_data) % 2 == 0 and int(get_data) > 20:
#     print("Even number and greater than 20")
# elif int(get_data) % 2 !=0 and int(get_data) > 20:
#     print("odd number and greater than 20")
# else:
#      print("Number is less than 20")


# BLOCK OF CODE
# loop
# cracker = 0
# while (cracker < 5):
#     print("cracker is less than 5")
#     cracker += 1

# num = 20
# num += 3
# print(num)

# slicing
# test ="blue sky"
# test1 = test[2 : : 5]
# print(test1)

# num = [30, 45, 60, 75]
# num1 = num[0 : 3 : 2]
# print(num1)

# formatting
# weather = "sunny"
# temperature = 40
# weather_report = "it is quite {} with a temperature of {} degrees".format(weather,temperature)
# weather_report = f"it is quite {weather} with a temperature of {temperature} degrees"
# print(weather_report)

# weather = "cloudy"
# temperature = 31
# print(weather_report)

# when = 'nation\'s crudeoil'
# print(when)

# Methods
# day = "it is quite"
# day1 = day.title()
# print(day1)

# day2 = day.startswith("I")
# print(day2)

# day3 = day.index("is")
# print(day3)

# day4 = day.find("quite")
# print(day4)

# day5 = day.split("s")
# print(day5)

# day6 = "sunny".join(day)
# print(day6)

# day7 = day.count("t")
# print(day7)

# day8 = day.replace("quite", "red")
# print(day8)

# day9 = day.strip("quite")
# print(day9)

# list methods
# Month = ["false", "true", 77, 99.4, True]
# Month = Month.clear()
# print(Month)

# list_1 = [12, 3, 5, 7]
# Month.extend(list_1)
# print(Month)

# Month.remove(77)
# print(Month)

# Month.append(False)
# print(Month)

# mon = Month.copy()
# print(mon)

# Month.insert(3, 88)
# print(Month)

# Month.pop()
# print(Month)

# Month.reverse()
# print(Month)

# Month = {"false", "true", 77, 99.4, True}
# Month.discard("true")
# print(Month)

# list_1 = {12, 3, 77, 7}
# mon = Month.union(list_1)
# print(mon)

# Month.update(list_1)
# print(Month)

# mon = Month.difference(list_1)
# print(mon)

# mon = Month.isdisjoint(list_1)
# print(mon)

# mon = Month.symmetric_difference(list_1)
# print(mon)

# diction = {“Pet”: “Dog”, “Colour”: “Brown”}
# my_diction["colour"] = "Black"
# print(diction)

# To know the type of data
# vas = 44
# print(type(vas))

# vas = str(vas)
# print(vas)

# sa = type(vas)
# print(sa)

# hat = 78
# print(type(hat))

# hat = str(hat)
# print(hat)

# print(type(hat))

# add = 78 + 4 * 18 - 23**4
# print(add)

# yam = 1500
# eggs = 1100
# cost = yam + eggs < 2450 or eggs/2 > 1/3*yam
# print(cost)

fall = [21,67,24,94,21,55,67,88,88,92,20,45,55]
fall2 = set(fall)
# print(fall2)

# fall2 = list(fall2)
# print(fall2)

# fall2.sort()
# print(fall2)

# fall2.pop(1)
# print(fall2)

# tup = (51, 69, 64, 30, 79, 20, 4, 90)
# tup = list(tup)
# # print(tup)

# tup.sort()
# print(tup)

# tup2 = tup.pop(5)
# print(tup2)

# tup.insert(2, tup2)
# print(tup)


# lis = [13,14, 48, 9, 98, 77, 34, 45, 6]
# lis2 = [22, 90,41, 53, 66, 14, 19, 7, 72, 54]
# print(lis[0 : : 2])
# print(lis2[1 : : 2])
# full_list = lis[0 : : 2] + lis2[1 : : 2]
# print(full_list)

# first_iterble = [2, 4, 6, 8]
# second = ["a", "b", "c", "d"]
# third_iterable = zip(first_iterble, second)
# print(list(third_iterable))

# sim = enumerate(second)
# print(list(sim))

# my_adder = lambda x, y,z : x**2 + y + z
# print(my_adder(5,6,7))

# my_map = map(lambda x : x +70, [20,40,60])
# print(list(my_map))

# covert string to integer using map
# jam = ('3', '5', '8', '10')
# jam2 = map(lambda x : int(x), jam)
# print(list(jam2))

# # filter (what will give you remainder)
# num = [20, 45, 60, 75, 98]
# my_filter = filter(lambda x : x % 2 != 0, num)
# print(list(my_filter))

# my_num = range (1,8)
# print(list(my_num))

# LOOPS!!!!
# cracker = 0
# while (cracker < 5)
#     if cracker == 3
#         print("This is my ride outta the loop!")
#         break
#     else:
#         print("cracker is less than 5")
#         cracker += 1

#  TASK (FOR PASSWORD AUTHORISATION)
# get_password1 = input("Enter password here: ")
# while True:
#      get_password2 = input("Repeat password here: ")
#      if get_password1 == get_password2:
#          print("sign up successful")
#          break
# else:
#         pass

# get_password1 = input("Enter password here: ")
# limit = 0
# while (limit < 2):
#      get_password2 = input("Repeat password here: ")
#      if get_password1 == get_password2:
#          print("login successful")
#          break
# else:
#         limit += 1

# # class task
# figure = input("input figures here")
# figure = figure.split(" ")
# fig = map(lambda a: int(a), figure)
# fid = list(fig)
# print(fid)

# import random as rd
# rand = rd.randrange(fid[0], fid[1])
# # print(rand)

# while True:
#     guess_number = input("Guess number:")
#     guess_number = int(guess_number)
#     if guess_number == rand:
#         print("YOU WIN!!!")
#         break
#     elif guess_number < rand:
#         print("Hint: YOUR NUMBER IS LESS!!!")
#     elif guess_number > rand:
#         print("Hint: YOUR NUMBER IS MORE!!1")
#     else:
#         pass

#  FOR LOOP
# THIS IS INDEPENDENT
# entry_data = "Universe"
# for a in entry_data:
#     print("Home for all!")

# THIS IS DEPENDENT
# new_list = ["pop", "rock", "country"]
# for item in new_list:
#     print(item)

# # FOR LOOP WITH ENUMERATE
# names = ["sheldon", "penny", "Howard", "Leonard", "Rajesh"]
# for index, item in enumerate(names):
#     print(index, item)

# FOR EVEN DECREASE BY 10% AND ODD INCREASE BY 10%
# lisa = input("numbers")
# lisa = lisa.split(" ")
# lis = map(lambda a: int(a), lisa)
# lid = list(lis)
# print(lid)

# for index, entry in enumerate(lis):
#     if entry % 2 == 0:
#         lis[index] = 0.9 * entry
#         print(list[index])
#     elif entry % 2 != 0:
#         lis[index] = 1.1 * entry
#         print(lis[index])
#     else:
#         pass    

# Assignment 1
# get_data = input("Enter integers here: ")
# con_list = get_data.split(" ")
# real_integers = list(map(lambda a : int(a), con_list))
# odd_numbers = list(filter(lambda a: a % 2, real_integers))

# no_of_inputs = len(real_integers)
# no_of_odd = len(odd_numbers)
# no_of_even = no_of_inputs - no_of_odd
# print(f"There are {no_of_odd} odd numbers.")
# print(f"There are {no_of_even} even numbers")

# odd = 0
# even = 0
# for entry in real_integers:
#     if entry % 2 == 0:
#         even += 1
#     elif entry % 2 != 0:
#         odd += 1
#     else:
#         pass

# print("there are {} odd numbers".format (odd))
# print(f"there are {even} even numbers")

# Assignment 2
# ment_data = input()
# con_list = ment_data.split(" ")
# con = "".join(con_list)
# print(con)
# lend = len(con)
# co = list(filter(lambda a : a.isalpha(),con))
# land = len(co) 
# ans = lend - land
# print(f"thare are {land} letters")
# print(f"there are {ans} digits")

# TO COUNT THE NUMBER OF DIGIT.
# To convert int to str
# get_fig = 1000000
# get = str(get_fig)
# gett = list(map(lambda a : a.isdigit(), get))
# grt = len(gett)
# print(grt)

# this procedure for float and to ignore decimal place
# fig_list = 535444.776544
# fig_list = str(fig_list)
# figs = fig_list.replace(".", "")
# fig_list = fig_list.split(".")
# fig = "".join(fig_list)
# print(len(fig))
# fi = list(map(lamb a : a.isdigit(), fig))
# fin = len(fi)
# print(fin)

# this procedure for reversal
# Write a program that takes in integers from the user and print them one after the other in reverse order
# joke_data = input()
# joke = joke_data.split (" ")
# jokes = list(joke)
# jokes.reverse()
# print(jokes.reverse)

# from datetime import datetime as dt
# Write a program that takes in a date:-25/12/2021 converts it to an actual date and add the time.
# print(xmas_time)
# xmass_time = dt.now().hour
# xmass_time = str(xmass_time)
# print(xmass_time)
# ass_time = dt.now().minute
# ass_time = str(ass_time)
# print(ass_time)
# ss_time = dt.now().second
# ss_time = str(ss_time)
# sn = xmas_time + "/" + xmass_time + "/" + ass_time  + "/" + ss_time
# print(sn)
# as_time = dt.strptime(sn,"%d/%m/%Y/%H/%M/%S")
# print(as_time)

# TASK: write a program that takes in "Jun 12 2021 3:30PM" and turns it into an actual date and time.
# mean_time = input()
# ean_time = dt.strptime(mean_time, "%d %b %Y %I:%M%p")
# print(ean_time)

# LIST COMPREHENSION
# Always return list as long as it does not contain a print
# it is a quick format
# [expression for item in iterable]
# Add 2 to the scores
scores = [42, 53, 61, 81, 57]
upgraded_scores = [ num + 2 for num in scores]
# print(upgraded_scores)
# Select the odd numbers
upgraded= [ num + 2 for num in scores if num % 2 != 0]
# print(upgraded)

# LOOPS REVISION
# TO COUNT DOWN 1 TO 20
for i in range(21):
    print(i)

# for t in range(20, 0, -2):
    # print(t)

# TO BRING OUT/SLEEP THE NUMBER AFTER EVERY ONE SEC
import time

# for i in range (20):
#     print(i)
#     time.sleep(1)

# TO HAVE DOUBLE NUMBERS SIDE TO SIDE USE THIS:
# KNOW THAT IT WILL STOP AT A NUMBER BEFORE
# for i in range (10):
#     for j in range(10):
#         for k in range(60):
#             for l in range(60):

#                 print(i, ":", j, ":", k, ":", l)
#                 time.sleep(1)


# for i in range (10, 0, -1):
#     for j in range(10, 0, -1):
#         for k in range(60, 0, -1):
#             for l in range(60, 0, -1):

#                 print(i, ":", j, ":", k, ":", l)
#                 time.sleep(1)


# TRYING TO FIND MISSING NUMBERS
# ADD SAME NUMBER THREE TIMES
# INDEX OUT THE LAST NUMBER(PLACE HOLDER)
# multiply the last number times 3

for i in range(1, 1000):
    sum_num = i + i + i

    place_holder = str(i)[-1]
    triple_placeholder = place_holder * 3

    if int(triple_placeholder) == sum_num:
        # print("HURRAY OUR NUM IS :", i, "->", sum_num)
        break 
    # print(i, sum_num, place_holder, triple_placeholder)

# FILTER
# names = ["ali", "kunle","bisi"] 

# for name in names:
#       print(f"Hi there {name} this bundle is specially for you.")