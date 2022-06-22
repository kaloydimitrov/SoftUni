from collections import deque

vowels = deque(input().split())
consonants = input().split()

words_original = ["rose", "tulip", "lotus", "daffodil"]

words = {
    0: "rose",
    1: "tulip",
    2: "lotus",
    3: "daffodil"
}

removed_key_word = 0
word_found = False

while not word_found:
    if len(vowels) == 0 or len(consonants) == 0:
        print("Cannot find any word!")
        break
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for key, word in words.items():
        if current_vowel in word:
            words[key] = words[key].replace(current_vowel, "")
        if current_consonant in word:
            words[key] = words[key].replace(current_consonant, "")

        if not words[key]:
            removed_key_word = key
            word_found = True

if word_found:
    print(f"Word found: {words_original[removed_key_word]}")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
