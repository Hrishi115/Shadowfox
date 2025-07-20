import random

# List of words with hints
words = [
    ["python", "A popular programming language"],
    ["astronaut", "A person who travels in space"],
    ["guitar", "A stringed musical instrument"],
    ["volcano", "A mountain that erupts"],
    ["jungle", "A dense forest with wild animals"],
    ["diamond", "A precious, hard gemstone"],
    ["ocean", "A large body of salt water"],
    ["chocolate", "A sweet made from cocoa"],
    ["kangaroo", "An animal that hops and carries babies in a pouch"],
    ["pyramid", "A triangular structure in Egypt"],
    ["island", "Land surrounded by water"],
    ["robot", "A machine that can perform tasks"],
    ["rainbow", "A colorful arc in the sky after rain"],
    ["whistle", "A sound made by blowing air through lips or a device"],
    ["library", "A place full of books"],
    ["vaccine", "A medicine to prevent illness"],
    ["bicycle", "A two-wheeled mode of transport"],
    ["mountain", "A very high hill"],
    ["sandwich", "Food made with two slices of bread"],
    ["pencil", "A tool for writing or drawing"]
]

# Choose random word
word, hint = random.choice(words)
hidden_word = list("_" * len(word))

guessed_letters = []
mistakes = 0
max_mistakes = 6

hangman_stages = ["", " O", "O\n |", "O\n/|", "O\n/|\\", "O\n/|\\\n/", "O\n/|\\\n/ \\"]

# Game loop
while mistakes < max_mistakes and "_" in hidden_word:
    print(f"\nHint: {hint}")
    print("Word: " + " ".join(hidden_word))
    print("Hangman:\n" + hangman_stages[mistakes])
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                hidden_word[i] = guess
        print("Correct!")
    else:
        mistakes += 1
        print("Wrong!")

# Final result
if "_" not in hidden_word:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)
    print("Final Hangman:\n" + hangman_stages[mistakes])