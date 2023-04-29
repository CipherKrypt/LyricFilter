"""
A Python Script that can encode a file using Caesar Cipher.
Compares the encoded text with a list of encoded explicit words.
This step is taken to shield readers of this code from explicit content
as a list of explicit words is required to check for hits.

AUTHOR: Sandro Sujith
DATE  : 29-04-2023
"""
import colorama
from termcolor import colored

colorama.init()  # initialize colorama for colored output

# Explicit word list is stored in cipher to protect reader from explicit content
explicit_words = ["KZHP", "KZHPNS", "KZHPNS'", "KZHPNSL", "GNYHM", "GNYHMNS'", "RTYMJWKZHPNS'", "RTYMJWKZHPNSL" , "KFLLTYX", "KFLX" , "LFD", "XJC", "SFPJI", "SZIJ", "UNXXNS'"]


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
    lyrics_ciphered = caesar_cipher(lyrics.upper())

    # Write ciphered lyrics to same file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(lyrics_ciphered)

# Takes file name and an additional list of explicit words and checks for hits
def check_explicit(filename, word_list:list = None):
    global explicit_words
    if word_list != None:
        wordList = []
        for word in word_list:
            wordList.append(caesar_cipher(word))
        
        explicit_words = set(explicit_words + wordList)

    # Read lyrics from file
    with open(filename, "r", encoding="utf-8") as file:
        lyrics = file.read()

    # Check for explicit words
    found_explicit = False
    hit = 0
    for word in lyrics.split():
        if word in explicit_words:
            
            hit+=1
    if hit > 0:
        found_explicit = True

    # Returns if the lyric contains explicit words and number of hits
    return (found_explicit, hit)

# Gets name of song and filename 
def check_lyric(name, filename):
    process_lyrics(filename)
    
    result = check_explicit(filename, explicit_words)
    # Print result in terminal
    if result[0]:
        print(colored(f"{name} - Explicit   Hits: {result[1]}", "red"))
    else:
        print(colored(f"{name} - Clear", "green"))

if __name__ == "__main__":
    # User_Input = Artist Name in Title case with the second name in lower case
    Artist_name = input("Enter Artist Name : ")
    # User_Input = Song Name in lowercase
    Song_name = input("Song name : ")
    from lyric_scraper import *
    main(Artist_name, Song_name)
    process_lyrics('lyrics.txt')
    





