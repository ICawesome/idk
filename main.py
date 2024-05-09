print("\n\n")

smart = None
dumb = None
lazy = None
diligent = None

print("hello, welcome to my thingy, about grades and students and stuff, idk.  for the first ones, any non-yes answer is no")
answer = input("are you smart? ")
if answer == 'y' or answer == 'yes' or answer == 'Yes':
    smart = True
else :
    answer = input("are you dumb? ")
    if answer == 'y' or answer == 'yes' or answer == 'Yes':
        dumb = True
    else:
        smart = False

answer = input("are you lazy? ")
if answer == 'y' or answer == 'yes' or answer == 'Yes':
    lazy = True
else:  
    answer = input("are you diligent? ")
    if answer == 'y' or answer == 'yes' or answer == 'Yes':
        diligent = True
    else:
        lazy = False 

proficiency = input("are you better at ELA, math, or are you bad at both? (answer with ELA, math, or bad) ")
while proficiency != "ELA" and proficiency != "math" and proficiency != "bad":
    print("that wasn't one of the options")
    proficiency = input("are you better at ELA, math, or are you bad at both? (answer with ELA, math, or bad) ")

print("\n")
if smart and lazy:
    print("you are a straight A student with maybe some variation in classes that assign more homework.")
if smart and not(lazy) and not(diligent):
    print("you are a straight A student.")
if smart and diligent:
    print("you are the straight A student, the best of the class, the best student in all of your classes.")
if not(smart) and not(dumb) and lazy:
    print("you are probably a below average student, but not a failing one.")
if not(smart) and not(dumb) and not(lazy) and not(diligent):
    print("average student")
if not(smart) and not(dumb) and diligent:
    print("above average student, maybe straight A student depending on how diligent.")
if dumb and lazy:
    print("that one kid that never pays attention and just plays games. L student")
if dumb and not(lazy) and not(diligent):
    print("below average student, C student probably")
if dumb and diligent:
    print("B student probably")


if proficiency == "ELA":
    print("you have better grades in english classes, and maybe the more creative classes")
if proficiency == "math":
    print("you have better grades in math classes and classes that use math, you might also be better at the more logical classes")
if proficiency == "bad":
    print("you have no proficiencies")



print("\n\n")
