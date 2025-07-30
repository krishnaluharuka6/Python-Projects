from time import *
import random as r

def mistake(test_input, user_input):
    error = 0
    for i in range(len(test_input)):
        try:
            if test_input[i] != user_input[i]:
                error = error + 1
        except:
            error += 1
    return error


def speed_time(time_start, time_end, user_input):
    time_delay = time_end - time_start
    time_roundoff = round(time_delay,2)
    speed = len(user_input)/time_roundoff
    return round(speed)

test = ["Hey! if you are a human show some humanity","lol","are u sure?"]

test1 = r.choice(test)
print("***** Typing speed calculator *****")
print(test1)
print()
print()
time_1 = time()
testinput = input("Enter:")
time_2 = time()

print(" Speed : ", speed_time(time_1, time_2, testinput),"words/seconds")

print("Error:", mistake(test1, testinput))


