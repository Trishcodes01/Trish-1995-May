# FUNCTIONS
# WHAT IS INSIDE FUNCTION MUST BE THE BUSINESS/BASIC LOGIC
# LET IT DO ONE THING

# def rocket(a):
#     print(a + 10)  
# rocket(5)

# def rocket():
#     print(5 + 10)   
# rocket()

import time
# WE USED DEF SO THAT WE CAN CALL IT "USELESS"
# def useless():
#     for i in range (10):
#          for j in range(10):
#              for k in range(60):
#                  for l in range(60):

#                      print(i, ":", j, ":", k, ":", l)
#                      time.sleep(1)

# useless()

# WRITTING AN ARGUMENT(hrs, mins, secs) INSIDE THE FUNCTION USE THIS:
# NOW ARGUMENTS ARE REQUIRED FOR PROPOGATION
# STOPPING AT 11 BECAUSE 10 + 2 = 12, MEANING IT STOPS A NUMBER BEFORE IT

# def useless2(hours, mins, secs):
#     for i in range(hours+2):
#          for j in range(mins+2):
#              for k in range(secs+2):

#                 print(i, ":", j, ":", k)

# useless2(2, 10, 6)


# THIS PROCESS TO APPLY INCREMENT AT A SPOT TO REFLECT IN SEVERAL PLACES
# RESTRUCTURE 
# FILTER ALLOWS TO BRING VARIALE IN ACTION

# def increment(num):
#     return num + 3

# print(increment(5))

# def restructure(hours, mins, secs):
#     return f"{hours}hours {mins}mins {secs}secs"


# def useless2(hours, mins, secs):
#     for i in range(increment(hours)):
#          for j in range(increment(mins)):
#              for k in range(increment(secs)):

#                 # print(i, ":", j, ":", k)
#                 print(restructure(i,j,k)) 

# useless2(2, 10, 6)





