import string
import sys
import os
import time

print(r'''
   ____                        _        ____               
  / ___|  _ __   __ _    ___  | | __   |  _ \   __ _   ___   ___ 
 | |     | '__/ / _` |  / __| | |/ /   | |_) | / _` | / __/ / __|
 | |___  | |   | (_| | | (__  |   <    |  __/ | (_| | \__ \ \__ \
  \____| |_|    \__,_|  \___| |_|\_\   |_|     \__,_| |___/ |___/
                                                 
''')


pas = input('Enter the password to continue: ')

sug = []

#length

pasl = len(pas)

if pasl < 8:
    sug.append(0)
elif pasl >= 12:
    sug.append(1)
elif pasl > 12:
    sug.append(2)

#char variety

up = sum(a.isupper() for a in pas)
low = sum(a.islower() for a in pas)
num = sum(a.isdigit() for a in pas)
sym = sum(c in string.punctuation for c in pas)

pasp = pasl//4


if up < pasp:
    u = " uppercase letters"
    if 3 not in sug:
        sug.append(3)
else:
    u = ""

if low < pasp:
    l = " lowercase letters"
    if 3 not in sug:
        sug.append(3)
else:
    l = ""

if num < pasp:
    n = " numbers"
    if 3 not in sug:
        sug.append(3)
else:
    n = ""

if sym < pasp:
    s = " symbols."
    if 3 not in sug:
        sug.append(3)
else:
    s = "."

if 3 not in sug:
    sug.append(4)


#wordlists

script_dir = os.path.dirname(os.path.abspath(__file__))
wordlists_dir = os.path.join(script_dir, "../wordlists")

wl = [
    os.path.join(wordlists_dir, "indian-passwords.txt"),
    os.path.join(wordlists_dir, "indian-passwords-length8-20.txt"),
    os.path.join(wordlists_dir, "rockyou_aa"),
    os.path.join(wordlists_dir, "rockyou_ab"),
    os.path.join(wordlists_dir, "rockyou_ac")
]


# for i in tqdm(range(100000)):
#     ...
#     time.sleep(0.0001)

# exit()


found = False
current_word = ""

for path in wl:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                word = line.strip()
                print(f"\rLooking in wordlists: {word[:50]:<50}", end="", flush=True)
                if word == pas:
                    found = True
                    break
        if found:
            break
    except FileNotFoundError:
        continue

print("\r" + " " * 70, end="\r")

if found:
    print(f"Found: {pas}")
    sug.append(5)
else:
    sug.append(6)




#suggestions

suggestions = [
    #length
    "Length is too short. Consider using at least 8 or more than 12 characters.",
    "Length is okay, but you might want to increase it for better security.",
    "Length is absolutely fine. You can use it as is.",

    #char variety
    "Lacks variety in caharacters. Try including more",
    "Has a good variety of characters.",

    #wordlist
    "Present in a list of commonly used passwords. Consider using a more unique password.",
    "Not present in a list of commonly used passwords. Good choice!",

    #char position
    "Try to avoid using characters in repeated positions, like 'aaaa' or '1111'.",
    "Good character position. No repeated patterns found.",
    "Try to avoid starting with a number or a special character. Starting with a letter is generally better.",
    
    #personal info
    "Consider avoiding personal information like names, birthdays, or addresses in your password.",
    "No personal information found in the password. Good job!",

    #brute force time estimation
    "Password is weak and can be cracked in less than a minute. Consider using a stronger password.",
    "Password is moderate and can be cracked in a few hours. Consider strengthening it.",
    "Password is strong and would take years to crack. Good choice!",

]

print("\nSummary:")

for ind in sug:
    if ind == 3:
        print(suggestions[ind]+u+l+n+s)
    else:
        print(suggestions[ind])

print()
