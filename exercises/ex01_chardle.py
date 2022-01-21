"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730461954"

count = 0

word_choice: str = input("Enter a 5-character word: ")
if len(word_choice) != 5:
    print("error")
    exit()

single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("error")
    exit()

print("searching for " + single_character + " in " + word_choice)

if single_character in word_choice:
    index = str(word_choice.find(single_character))
    print(single_character + " found at index " + index)
    count = count + 1
    if word_choice.count(single_character) > 1:
        index_two = str(word_choice.find(single_character, int(index) + 1,))
        print(single_character + " found at index " + index_two)
        count = count + 1 
        if word_choice.count(single_character) > 2:
            index_three = str(word_choice.find(single_character, int(index_two) + 1,))
            print(single_character + " found at index " + index_three)
            count = count + 1
            if word_choice.count(single_character) > 3:
                index_four = str(word_choice.find(single_character, int(index_three) + 1,))
                print(single_character + " found at index " + index_four)
                count = count + 1
                if word_choice.count(single_character) > 4:
                    index_five = str(word_choice.find(single_character, int(index_four) + 1,))
                    print(single_character + " found at index " + index_five)
                    count = count + 1

if count == 0:
    print("No instances of " + single_character + " found in " + word_choice)
else:
    if count == 1:
        print(str(count) + " instance of " + single_character + " found in " + word_choice)
    else:
        print(str(count) + " instances of " + single_character + " found in " + word_choice)
