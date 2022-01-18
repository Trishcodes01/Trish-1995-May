# USING THIS METHOD TO GUESS NUMBER RIGHT 
# \N USE TO GET SPACE
# RETURN TELLS THE FUNCTION WHAT TO DO\GIVE BACK

# SET PLAY LIMIT TO 10 TIMES MAX AND ALSO DISPLAY 10SECS THEN RESET
import random as rd

def collect_data():

    figure = input("input figures \n> ") 
    name = input("input name \n> ")

    figure = figure.split(" ")
    fig = map(lambda a: int(a), figure)
    fid = list(fig)
    print(fid)

    rand = rd.randrange(fid[0], fid[1])
    print(rand)
    return rand, name


# TO COUNT THE NUMBER OF TIME YOU TRY OUT SOMETHING
# ADD A COUNTER AND MAKE IT EMPTY AT FIRST
def play():

    tries = 0

    rand, name = collect_data()

    while True:
        guess_number = input("Guess number:")
        # TYPE CASTING
        guess_number = int(guess_number)   
        tries += 1 

        if guess_number == rand:
            print("YOU WIN!!!")
            break
        elif guess_number < rand:
            print("Hint: YOUR NUMBER IS LESS!!!")
        elif guess_number > rand:
            print("Hint: YOUR NUMBER IS MORE!!1")
        else:
            pass

    write_to_file(name, tries)
    # return name, tries

    # print("You tried :", tries, "times")
       
# play()


# w = clean the File and create another
# r = open the file for reading
# a = continue from where the file stops

# with open("database.csv", "a") as our_log_file:
#     name = "atha"
#     tries = 6
#     our_log_file.write(f"{name},{tries}")

# write to file means take any value and create a new file then input value inside it. e.g name and number
def write_to_file(name, tries):
    # CONTEXT MANAGER
    with open("database.csv", "a") as our_log_file:
        our_log_file.write(f"{name},{tries}\n")

    print("logged session.!!")

write_to_file("Tolu", 20)
play()

# def play_shot(name, tries):
#     name, tries = play()
#     with open("data.csv", "a", newline = "") as our_file:
#         our_file.write(f"{name}: {tries} \n")

import random as rd
import time

def play():

    limit = 1
    tries = 0

    rand, name = collect_data()

    while True:
        guess_number = input("Guess number:") # TYPE CASTING
        guess_number = int(guess_number)   
        tries += 1 # add a counter and make it empty at first
        limit += 1

        if guess_number == rand:
            print("YOU WIN!!!")
            break
        elif guess_number < rand:
            print("Hint: YOUR NUMBER IS LESS!!!")
        elif guess_number > rand:
            print("Hint: YOUR NUMBER IS MORE!!1")
        
        if limit == 10:
            print("You missed it ", tries, "times")
            print("We are now delaying you.")
            limit = 1
            time.sleep(10)

    write_to_file(name, tries)

print("Hello my name is : ", __name__)

if __name__ =="__main__":
    print("HEY THERE I AM THE MAIN MAN")
