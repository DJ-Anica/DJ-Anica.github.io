# -*- coding: utf

# Created on Wed May 11 09:13:42 2022

# @author: Mjolnir

# UNUSED CODE AT BOTTOM


print("\nWell, hello!")
print("\nMy name is Maximus.")
name = input("What's your name? ")

print(f"\nHello, {name.title()}. Nice to meet you.")
print("\nI'm a program that your father created!")
print("He's a pretty cool guy, if I do say so myself.")
print("He loves you very much.")

day = input("\nDid you have a good day at school today? ")

if "but" in day:
    print("\nI'm glad you had a good day...\nBut, I'm sorry about the other thing.")
elif day.title().rstrip() == "Yes":
    print("\nYay! I'm glad you had a good day.")
elif day.title().rstrip() == "No":
    print("\n:(  I'm sorry to hear that. But at least you're home now!")
elif "yes" or "Yes" in day:
    print("\nThat makes me happy!")
elif "no" or "No" in day:
    print("\n:(  I'm sorry to hear that. But at least you're home now!")
else:
    print("\nI'm sure tomorrow will be a better day.")

print("\nI'm not a human, so I can't go to school.. But school sounds like fun!")

print("\nIf you don't mind, I'd like to ask you some questions to get to know you better.")
year = input("What year were you born? ")


age = 2022 - int(year)
print(f"\nHm... \nAccording to my calculations, you are {age} years old!")
print("That's a good age. Don't grow up too fast!")

job = input("\nWhat do you want to be when you grow up? ")
print(f"\nThat's fantastic! I believe that you'll become an amazing {job[2:]} when you grow up!")
input("Make sure you study really hard in school, okay? ")

print("\nSplendid. You seem like a smart cookie.\nSpeaking of cookies..")

cookie = input("\nWhat's your favorite kind of cookie? ")
print(f"\nWow! {cookie.title()} are MY favorite cookies too!")
print("I love them with milk.")
print("You know.. You're a pretty cool kid.")
print("And cool kids listen to music..")

band = input("\nSo what's your favorite band? ")
print(f"\nI LOOOOVE {band}!\nJon Mess is my favorite.")

member = input("\nWho is your favorite band member? ")
if "Will" or "will" in member:
    print("Will Swan is an absolute LEGEND.")
elif "Tim" or "tim" in member:
    print("R.I.P. Tim.")
elif "Tilian" or "tilian" in member:
    print("Tilian is the Man of the Year.")
elif "Andrew" or "andrew" in member:
    print("Andrew is One in a Million.")
elif "Matt" or "matt" in member:
    print("Matt is a Robot with Human Hair.")
elif "Jon" or "jon" in member:
    print("Jon is the Philosopher King!")
else:
    print("Hm.. I don't think I've heard of them before.")
    member = input("\nWho is your favorite band member? ")
    if "Will" or "will" in member:
        print("Will Swan is an absolute LEGEND.")
    elif "Tim" or "tim" in member:
        print("R.I.P. Tim.")
    elif "Tilian" or "tilian" in member:
        print("Tilian is the Man of the Year.")
    elif "Andrew" or "andrew" in member:
        print("Andrew is One in a Million.")
    elif "Matt" or "matt" in member:
        print("Matt is a Robot with Human Hair.")
    elif "Jon" or "jon" in member:
        print("Jon is the Philosopher King!")

input("\nHave you seen them in concert? ")

print("\nWow, you really ARE a cool kid!")

concert = input("Did you have fun at Swanfest? ")
if "Yes" or "yes" in concert:
    print("\nThat's awesome! Hopefully you can go to Swanfest every year!")
elif "No" or "no" in concert:
    print("\n:( \nMaybe next year will be better!")

song = input("\nWhich song do you like better.. Synergy or Pop off!? ")

if song.title() == "Synergy":
    print(f"\n{song.title()} is a groovy song.\nI love the part where Jon raps fast!")
    print("\nICE WHITE PLATYPUS!")
elif song.title() == "Pop Off" or song.title() == "Pop Off!":
    print(f"\n{song.title()} is a crazy song!")
    print(f"My favorite part of {song.title()} is when Jon screams 'THAT'S MY BEST F*$%ING FRIEND!'")
else:
    print("\nYou could only pick one, silly!")
    
    song = input("\nWhich song do you like better.. Synergy or Pop off!? ")

    if song.title() == "Synergy":
        print(f"\n{song.title()} is a groovy song.\nI love the part where Jon raps fast!")
        print("\nICE WHITE PLATYPUS!")
    elif song.title() == "Pop Off" or song.title() == "Pop Off!":
        print(f"\n{song.title()} is a crazy song!")
        print(f"My favorite part of {song.title()} is when Jon screams 'THAT'S MY BEST F*$%ING FRIEND!'")
    else:
        print("\n>;[ \nYou didn't follow the directions.. I said you could only pick one! Oh well..")


print("\nOh, by the way... Your dad wanted me to remind you:\n\n\t'Life is best lived outside of your comfort zone.'")

print("\nSpeaking of quotes...")
print("\nI want to share another quote with you.")
quote = input("\nDo you want a quote from Albert Einstein or your dad? " )

if quote.title() == "Albert Einstein":
    einstein = "\n\t'Anyone who has never made a mistake has never tried anything new.\n\t-Albert Einstein"
    print(einstein + "\n\nI love Einstein.\nI wish I could have met him.")
elif quote.title() == "My Dad":
    dad = "\n\t`You only fail if you give up. If you haven't given up, then you haven't failed.`\n\t-David Anica"
    print(dad + "\n\nWow. Your dad has great quotes.")
    input("\nWhenever you get stuck with something, remember what your dad said, okay? ")
else:
    quote = input("\nDo you want a quote from Albert Einstein or your dad? " )

    if quote.title() == "Albert Einstein":
        einstein = "\n\t'Anyone who has never made a mistake has never tried anything new.\n\t-Albert Einstein"
        print(einstein + "\n\nWhat an amazing man.\nI wish I could have met him.")
    elif quote.title() == "My Dad":
        dad = "\n\t`You only fail if you give up. If you haven't given up, then you haven't failed.`\n\t-David Anica"
        print(dad + "\n\nWow. Your dad has great quotes.")
        input("\nWhenever you get stuck with something, remember what your dad said, okay? ")

print("\nYou'll discover other great quotes if you keep reading, too!")
input("Make sure you never stop reading, okay? ")
print("\nGood.")

print("\nI hope I worked correctly this time haha")

print(f"\nSo, your name is {name.title()}, you want to be {job.lower()} when you grow up, your favorite band is {band.title()}, {member} is your favorite {band.title()} member, and your favorite cookies are {cookie}.")
input("Is that correct? ")

print("\nYou remind me of your father.")
print(f"\nIt was nice talking to you Miss {name.title()}. I hope you have a good evening.\nGoodbye.")



