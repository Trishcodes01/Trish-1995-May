# A FUNCTION WONT EXECUTE A BLOCK OF CODE UNLESS YOU CALL IT.
# you can use any variable name
# THe number of pararmeter passed should be equal to the number of argument passed.
def basic():
    print("This is a pretty basic function")

basic()

# def rocket(a):
    # print(a + 10)
    
# rocket(5)
    
def password_1(a):
    print("a == password_2")
    password_1 = input("Enter password here")
    while True:   
       password_2 = input("repeat password here")
       if password_1 == password_2:
          print("login successful")
          break

password_1("password_2")   

