"""
A Python Script that can web scrape 'https://genius.com' for lyrics of a  song given the 
Artist name and Song name, and save the scraped text into the parsedhtml.txt file.
Cleans up the parsedhtml.txt file by removing unnecessary brackets 
and adding space or newline where neccessary, saves the resultant text into 'lyrics.txt'


AUTHOR: Sandro Sujith
DATE  : 28-04-2023
"""

import requests
from bs4 import BeautifulSoup
import re

def clean_up(file):
    # Read input file and store contents in a variable
    with open(file, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    # Remove square brackets and text between them 
    text = re.sub(r'\[.*?\]', '', text)
    # Add space before capitalized words as html parser cannot detect <br> tags
    cleaned_text = re.sub(r'(?<=[a-z])([A-Z])', "\n"+r'\1', text)

    # Write cleaned text to output file
    with open("lyrics.txt", "w", encoding="utf-8") as output_file:
        output_file.write(cleaned_text)


def format_text(artist:str, song:str):
    # Formats the given details into the form suitable for the URL
    # Artist name should be in title case but surname/last name should be in lowercase
    artist = artist[0].upper() + artist[1:].lower()
    # Song name should be lowercase
    song = song.lower()
    # Artist name and song name should be joined by a hyphen
    lyrics_url = artist+"-"+song

    # Formats symbols to suitable format for URL
    lyrics_url = lyrics_url.replace("&","and")
    lyrics_url = lyrics_url.replace("'","")

    # All spaces should be replaced with a hyphen
    return lyrics_url.replace(" ","-").rstrip('-')

def scrape(Artist_name, Song_name):
    # Formats the given details into the url of form 'https://genius.com/artist-song-lyrics'
    lyrics_url = format_text(Artist_name,Song_name)
    base_url = "https://genius.com/"+lyrics_url+"-lyrics" 
    print("Scraped URL:", base_url)

    result = requests.get(base_url) # Scrapes the result 

    soup = BeautifulSoup(result.text, "html.parser")
    # The Lyrics were found under the dic tag with class 'Lyrics__Container-sc-1ynbvzw-5 Dzxov'
    lyric_tag = soup.find_all("div", attrs={'class': 'Lyrics__Container-sc-1ynbvzw-5 Dzxov'})
    # Parses through all the child tags, reads their text and writes into the 'parsedhtml.txt' file
    with open("parsedhtml.txt", "w", encoding="utf-8") as file:
        for tags in lyric_tag:
            file.write(tags.text + "\n")
    file.close()
    clean_up('parsedhtml.txt')

if __name__ == "__main__":
    # User_Input = Artist Name in Title case with the second name in lower case
    Artist_name = input("Enter Artist Name : ")
    # User_Input = Song Name in lowercase
    Song_name = input("Song name : ")

    scrape(Artist_name, Song_name)