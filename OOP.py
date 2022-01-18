# Humankind is the class creation
# method has parenthesis while attribute doesnt.
# START WITH UPPER CASE
# skin, eyes, legs are attributes
# OBJECT SAME AS INSTANCE

# class Humankind:

#     skin = True
#     eyes = True
#     legs = True
#     species = "mammal"

# Human_kind = Humankind() #OBJECT CREATION CLASS INSTANTIATION
# another_name = Humankind() 
# # print(Human_kind)
# print(Human_kind.skin)
# print(another_name.skin)

# objects = []
# for i in range(10000):
#     objects.append(Humankind())

# print(objects)

# SELF: POINT TO CURRENT INSTANCE OF THAT CLASS
# SELF IS THE SAME AS OBJECT
# The first argument you use\input is self
# F IS USED WITH CURLY BRACES
# 1000 IS THE FREQUENCY
# 500 IS THE MINS

# import winsound, time, random, guess_game

# class Humankind: #CLASS CREATION

#     skin = True
#     eyes = True
#     legs = True
#     species = "mammal"

#     def describe(self):
#         print(f"Hello my species is {self.species}")

#     def makenoise(self):
#         print("HELLO !!!!!")
#         winsound.Beep(1000, 500)
#         time.sleep(1)
#         winsound.Beep(1000, 500)
#         time.sleep(1)
#         winsound.Beep(1000, 500)

# varname = Humankind()
# varname.describe()
# varname.makenoise()


# CREATE A CLASS OF CAT WITH ATTRIBUTES: names, fur colour, family AND METHOD DESCRIBE THAT PRINTS "hello i am a cat, my fur colour is {fur colour} and my name is {name}."
# class Cat:

#     name = "Catches"
#     fur_colour = "Burgundy" 
#     family = "Ragdoll"
    
#     def describe(self):
#         print(f"Hello i am a cat, my fur_colour is {self.fur_colour} and my name is {self.family}")

# favname = Cat()
# favname.describe()

# INSTANCE ATTRIBUTES: ARE DIFFERENT AND UNIQUE IN IT OWN WAY to each object you create
# CLASS ATTRIBUTES: IT IS A GENERAL TERM/CLASSIFICATION. E.G ALL DOGS BARK
# class Person:

#     #  CLASS ATTRIBUTE
#     species = "Homo-Sapien"
#     _class = "Mammal"

#     def __init__(self, name, complexion, height):
#         self.name =name
#         self.complexion = complexion
#         self.height = height
#         self.voice_freq = random.randint(50, 1500)

#     def say_something(self):
#         print(f"Hello, my name is {self.name}. \n I am a {self._class},{self.complexion}, and my height is {self.height}")
#         winsound.Beep(self.voice_freq, 500)
#         time.sleep(0.5)
#         winsound.Beep(self.voice_freq, 500)
#         time.sleep(0.5)
#         winsound.Beep(self.voice_freq, 500) 

# person1 = Person(name = "Ade", complexion=" Brown skin", height="5ft7")
# person1.say_something()

# person2 = Person(name = "segun", complexion="fair skin", height="6ft2")
# person2.say_something()


# class EthnicMeal:
#     def igbo(self):  #instance method
#           print("Rice")

#     def yoruba(self):
#         print("Amala")

#     def hausa(self):
#         print("Two shinkafa")

# meal_one = EthnicMeal()
# meal_one.hausa()

# class Student:
#    def __init__(self, name, gender, age):
#     self.name = name
#     self.gender = gender
#     self.age = age        

#     def get_name(self):             #accesor instance method
#         return self.name

#     def get_gender(self):
#         return self.gender

#     def get_age(self):
#         return self.age


#     def set_name(self, value):          #mutator instance method
#         self.name = value

#     def set_gender(self, value):
#         self.gender = value

#     def set_age(self, value):
#         self.age = value 

# stu_one = Student("Kelsey", "Female", 22)
# stu_two = Student("Brian", "Male", 35)
# stu_three = Student("Ernie", "Male", 27)

# print(stu_one.get_name())

# print(stu_two.get_age())
# stu_two.set_age(33)
# print(stu_two.get_age())



# class School:
#     no_of_students = 0
#     sum_of_scores = 0


# instance method are student name and student score and you use initialation
#     def __init__(self, student_name, student_score):
#        self.student_name = student_name
#        self.student_score = student_score
#        School.increase_count()
#        School.sum_of_scores += self.get_student_score() 

#     def get_student_name(self):
#         return self.student_name

#     def get_student_score(self):
#         return self.student_score       #this is an instance method

#     def set_student_name(self, value):
#         self.student_name = value

#     def set_student_score(self, value):
#         self.student_score = value

#     @classmethod                                      #decorator is used to show class method
#     def increase_count(cls):     #cls for class method.
#         cls.no_of_students += 1

#     @classmethod
#     def average_score(cls):
#         output = cls.sum_of_scores / cls.no_of_students
#         return round(output, 2)



# edu_one = School("Emeka", 24.56)
# # edu_one.increase_count()
# edu_two = School("Oluwagbemisola", 99.00)
# # edu_two.increase_count()
# # print(School.no_of_students)
# # print(School.average_score())

# instance_collection = [School("Ifeoma", 64.22), School("Musa", 76.99), School("Bamishe", 58.40)]
# print(instance_collection[1].get_student_score())

# A CLASS THAT TAKES IN USER'S PERSONAL INFORMATION AND WRITE IT INTO A CSV FILE" NAME, GENDER, AGE AND LOCATION IF THE USER CAN SUPPLY THE NAME AND AGE CORRECTLY CREATE  AN AVENUE TO CHANGE THE LOCATION.

# import csv
# class Info:

#     def __init__(self, name, gender, age, location):
#         self.name = name
#         self.gender = gender
#         self.age = age  
#         self.location = location   
#         self.User()


#     def User(self):
#         new_info = open("C:/Users/beatrice1/Desktop/UNIVELCITY CLASS/Info.csv", mode = "w", encoding = "utf-8", newline = "")
#         pen = csv.writer(new_info)
#         pen.writerow(["name", "gender", "age", "location"])
#         pen.writerow([self.name, self.gender, self.age, self.location])


# info_two = Info(input("Input name here:"), input("Input gender here:"), input("Input age here:",), input("Input location here:"))
# print(info_two)

    # def get_name(self):
    #     return self.name

    # def get_gender(self):
    #     return self.gender  

    # def get_age(self):
    #     return self.age

    # def get_location(self):
    #     return self.age

    # def set_name(self, value):
    #     self.name = value

    # def set_gender(self, value):
    #     self.gender = value

    # def set_age(self, value):
    #     self.age = value

    # def set_location(self, value):
    #     self.location = value


# class Staff:
    
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age  
        
#     def status(self):
#         print("I am a registered staff")

#     def get_name(self):
#         return self.name

# class Manager(Staff):
#     def __init__(self,name, gender, age, department, level):
#        super().__init__(name, gender, age)
#        self.department = department
#        self.level = level

#     def role_dist(self):
#         print("I distribution roles!")

# m_one = Manager("Trish", "Female", 25)
# m_one = Manager("Aliyah", "Female", 30, "I.T", 3) #combination
# m_one.role_dist()       #this is a method
# m_one.status()
# # TO GET THE NAME YOU HAVE TO CALL IT FROM THE STAFF i.e from get name
# print(m_one.get_name())
# print(m_one.get_name())
# print(m_one.get_age())
# print(m_one.get_gender())
# print(m_one.get_department())

# HAVE ACCESSING TO BOTH PARENT AND CHILD "INIT"(INSTANCE METHOD) YOU USE SUPER

print("Hello my name is : ", __name__)