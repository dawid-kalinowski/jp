import random

# Load words from file
words = {}
with open("words.txt", "r") as file:
    for line in file:
        polish, japanese = line.strip().split(" - ")
        words[polish] = japanese

# Get all Japanese words
japanese_words = list(words.values())

correct_count = 0
total_count = len(japanese_words)
word_number = 0

while japanese_words:
    # Increment word number
    word_number += 1
    # Get a random Japanese word
    japanese_word = random.choice(japanese_words)

    # Get its Polish translation
    correct_translation = next(polish for polish, japanese in words.items() if japanese == japanese_word)

    # Get user input
    print(f"({word_number}/{total_count})", end=" ")
    user_translation = input(japanese_word + ": ")


    # Check if the user's input matches the correct translation
    if user_translation.strip() == correct_translation:
        print("Tak!")
        correct_count += 1
    else:
        print("Nie do końca, " + correct_translation)

    # Remove the word from the list
    japanese_words.remove(japanese_word)

print("You have completed the quiz.")
print("Accuracy:", (correct_count / total_count) * 100, "%")