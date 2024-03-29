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
import logging

logging.basicConfig(filename='lyrics_scrapper.log', encoding='utf-8', level=logging.DEBUG)


def clean_up(file):
    logging.debug('running clean_up()')
    # Read input file and store contents in a variable
    logging.debug('opening html file and cleaning')
    with open(f'{file}.txt', "r", encoding="utf-8") as input_file:
        text = input_file.read()

    # Remove square brackets and text between them 
    text = re.sub(r'\[.*?\]', '', text)
    # Add space before capitalized words as html parser cannot detect <br> tags
    cleaned_text = re.sub(r'(?<=[a-z])([A-Z])', "\n"+r'\1', text)

    logging.debug(f'Cleaned Lyrics Text \n {cleaned_text} \n')
    logging.debug('Writing clean file')
    # Write cleaned text to output file
    with open(f'{file}.txt', "w", encoding="utf-8") as output_file:
        output_file.write(cleaned_text)


def format_text(artist:str, song:str):
    logging.debug('running format_text()')

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
    lyrics_url = lyrics_url.replace(" ","-").rstrip('-')
    

    # All spaces should be replaced with a hyphen
    return lyrics_url

def scrape(Artist_name:str, Song_name:str, output_file:str) -> None: 
    logging.debug('running scrape()')
    # Formats the given details into the url of form 'https://genius.com/artist-song-lyrics'
    lyrics_url = format_text(Artist_name,Song_name)
    base_url = "https://genius.com/"+lyrics_url+"-lyrics"
    logging.debug(f'The lyrics URL generated: {base_url}')

    result = requests.get(base_url) # Scrapes the result 

    soup = BeautifulSoup(result.text, "html.parser")
    # The Lyrics were found under the dic tag with class 'Lyrics__Container-sc-1ynbvzw-5 Dzxov'
    lyric_tag = soup.find_all("div", attrs={'class': 'Lyrics__Container-sc-1ynbvzw-1 kUgSbL'})
    # Parses through all the child tags, reads their text and writes into the 'parsedhtml.txt' file
    with open(f"{output_file}.txt", "w", encoding="utf-8") as file:
        for tags in lyric_tag:
            file.write(tags.text + "\n")
            

    file.close()
    clean_up(output_file)
    return base_url

if __name__ == "__main__":
    # User_Input = Artist Name in Title case with the second name in lower case
    Artist_name = input("Enter Artist Name : ")
    # User_Input = Song Name in lowercase
    Song_name = input("Song name : ")

    scrape(Artist_name, Song_name, "lyrics")