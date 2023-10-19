import random

# Pilih lagu untuk diteka
songs = ("negaraku", "jalur gemilang", "malaysiaku gemilang", "tanggal 31", "keranamu malaysia")

def choose_random_song(songs):
    return random.choice(songs)

def scramble_song(song):
    # Convert the song to a list of characters
    characters = list(song)
    # Shuffle the characters
    random.shuffle(characters)
    return ''.join(characters)

def play_game():
    # Choose a random song
    random_song = choose_random_song(songs)
    scrambled_song = scramble_song(random_song)

    print("Welcome to the Music Guessing Game!")
    print("Here's a scrambled song title: " + scrambled_song)

    attempts = 3
    while attempts > 0:
        guess = input("Guess the song: ").lower()

        if guess == random_song:
            print("Congratulations! You guessed the song correctly.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong guess. You have {attempts} attempts left.")
            else:
                print("You're out of attempts. The correct answer was: " + random_song)
                break

if __name__ == "__main__":
    play_game()
