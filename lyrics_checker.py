"""
A Python Script that can encode a file using Caesar Cipher.

AUTHOR: Sandro Sujith
DATE  : 29-04-2023
"""
# Caesar cipher to encode lyrics
def caesar_cipher(text, key=5):
    # Caesar cipher implementation
    result = ''
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + key) % 26 + 65)
            result += shifted_char
        else:
            result += char
    return result

# Encodes lyrics with Caesar Cipher
def process_lyrics(filename):
    # Read lyrics from file
    with open(filename, "r", encoding="utf-8") as file:
        lyrics = file.read()
        if len(lyrics) == 0:
            raise Exception("Lyrics not found")

    # Apply Caesar cipher with key=5
    lyrics_ciphered = caesar_cipher(lyrics.upper(), 5)

    # Write ciphered lyrics to same file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(lyrics_ciphered)

if __name__ == "__main__":
    # User_Input = Artist Name in Title case with the second name in lower case
    Artist_name = input("Enter Artist Name : ")
    # User_Input = Song Name in lowercase
    Song_name = input("Song name : ")
    from lyric_scraper import *
    main(Artist_name, Song_name)
    process_lyrics('lyrics.txt')
    





