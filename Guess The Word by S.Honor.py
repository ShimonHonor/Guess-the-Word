import random
from words import animals, fruits, musical_instruments, stationary_objects

word_bank = {
    "Animal": animals,
    "Fruit": fruits,
    "Musical Instrument": musical_instruments,
    "Stationary Object": stationary_objects
}

num_players = int(input("Enter number of players: "))
players = [input(f"Enter name for Player {i+1}: ") for i in range(num_players)]
scores = {player: 0 for player in players}

all_words = [(word, category) for category, word_list in word_bank.items() for word in word_list]
random.shuffle(all_words)

max_words = int(input(f"Enter number of words to play (max {len(all_words)}): "))
if max_words > len(all_words):
    print("Not enough words in the bank. Game will use all available words instead.")
    max_words = len(all_words)

words = all_words[:max_words]

player_index = 0

for random_word, category in words:
    guessed_letters = set()
    chances = 5
    print(f"\nNew word chosen! Hint: It is a {category}")

    while chances > 0:
        display = ''.join([ch if ch.lower() in guessed_letters else '_' for ch in random_word])
        print("Word:", display, f"(Chances left: {chances})")

        if all(ch.lower() in guessed_letters for ch in random_word.lower()):
            print(f"Word fully guessed! It was '{random_word}'")
            break

        current_player = players[player_index]

        guess = ""
        while True:
            guess = input(f"{current_player}, enter a letter: ").lower()
            if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
                break
            print("Invalid guess. Try again.")

        guessed_letters.add(guess)

        if guess in random_word.lower():
            occurrences = random_word.lower().count(guess)
            scores[current_player] += occurrences
            print(f"Correct! {current_player} earns {occurrences} point(s).")
        else:
            chances -= 1
            print(f"Wrong! {current_player} loses a chance.")

        player_index = (player_index + 1) % num_players

    if chances == 0:
        print(f"Out of chances! The word was '{random_word}'")

print("\nGame Over! Final Scores:")
for player, score in scores.items():
    print(f"{player}: {score}")

winner = max(scores, key=scores.get)
print(f"Winner is {winner}!")