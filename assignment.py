# A
ribbon = []
for odd in range(148, 599):
    new_ribbon = str(odd)
    if (int(new_ribbon[0])%2!=0) and (int(new_ribbon[1])%2!=0) and (int(new_ribbon[2])%2!=0):
      ribbon.append(new_ribbon)
# print( ",".join(ribbon))

# B
joke_data = (7, 4, 6, 1, 5, 3)
jokes = list(joke_data)
jokes.reverse()
# print(jokes)

# C
jump = ("blOGGeR")
jump = list(jump)
jump.sort(reverse = True)
jumps = "".join(jump)
# print(jumps)

# D
num = {55, 99, 77, 44, 33, 88, 11, 66}
my_shot = filter(lambda x : x % 2 != 0, num)
# print(list(my_shot))
