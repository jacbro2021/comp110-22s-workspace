"""EX01 - Chardle - A cute step toward Wordle."""

_author_ = "730461954"

count = 0

word_choice: str = input("Enter a 5-character word: ")
if len(word_choice) != 5:
    print("exiting program due to user not following prompt.")
    exit()

single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("exiting program due to user not following prompt.")
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
                if word_choice.count(single_character) > 2:
                    index_five = str(word_choice.find(single_character, int(index_four) + 1,))
                    print(single_character + " found at index " + index_five)
                    count = count + 1
print(str(count) + " instances of " + single_character + " found in" + word_choice)
