import re, sys
from playsound import playsound


print("Enter the sentence so say the sentence")
print('Enter "exit" to exit')

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
            playsound("sounds/" + i + ".wav")
        except:
            missing_words_arr.append(i)
    print("Done!")
    
    missing_words = ", ".join(missing_words_arr)
    if len(missing_words) != 0:
        print("Missing words: " + missing_words)