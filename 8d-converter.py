import numpy as np
import wavio
import math
import sys

def write_sound(name,sound):
    rate = 48000
    wavio.write("8d_"+name,sound,rate,sampwidth=3)

def read_sound(name):
    return list(wavio.read(name).data)

def surround(name):
    s = read_sound(name)
    s2 = []
    if len(s[0]) == 2:
        for i in range(len(s)):
            s2.append([s[i][0] * math.sin(float(i/96000)),s[i][1] * math.cos(float(i/96000))])
    elif len(s[0]) == 1:
        for i in range(len(s)):
            s2.append([s[i][0] * math.sin(float(i/96000)),s[i][0] * math.cos(float(i/96000))])
    else:
        print("ERR: Invalid audio dimensions")
    return np.array(s2)


file = input("Enter song file name with extension: ")
print("Converting song...")
try:
    write_sound(file,surround(file))
except:
    print("Unknown error converting song.")

print("Finished.")

