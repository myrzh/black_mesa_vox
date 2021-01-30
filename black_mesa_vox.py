import re, sys
from playsound import playsound


while True:
    path0 = input("What audio files you want to use? Enter 'bms' to use Black Mesa files, enter 'hl1' to use Half-Life files: ")
    if path0 == "bms":
        path = "sounds_bms/"
        break
    elif path0 == "hl":
        path = "sounds_hl/"
        break
    else:
        print("Incorrect input! Try again")

print("Enter the sentence so say the sentence")
print("Enter 'exit' to exit")

while True:
    missing_words_arr = []
    sentence = input("Input: ")

    if sentence == "exit":
        sys.exit()
    if sentence.isspace() == True or len(sentence) == 0:
        print("Empty input! Try again")
        continue

    sentence.lower()
    sentence = re.sub(r'[^\w\s]','', sentence)
    words = sentence.split()

    try:
        words.index("for")
    except:
        pass
    else:
        words[words.index("for")] = "four"

    print("Processing...")
    for i in words:
        try:
            playsound(path + i + ".wav")
        except:
            missing_words_arr.append(i)
    print("Done!")
    
    missing_words = ", ".join(missing_words_arr)
    if len(missing_words) != 0:
        print("Missing words: " + missing_words)