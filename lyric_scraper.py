"""
A Python Script that can web scrape 'https://genius.com' for lyrics of a  song given the 
Artist name and Song name, and save the scraped text into the parsedhtml.txt file.


AUTHOR: Sandro Sujith
DATE  : 28-04-2023
"""

import requests
from bs4 import BeautifulSoup


def main(Artist_name, Song_name):
    # Formats the given details into the url of form 'https://genius.com/artist-song-lyrics'
    lyrics_url = Artist_name+"-"+Song_name
    lyrics_url = lyrics_url.replace(' ', '-')
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

if __name__ == "__main__":
    # User_Input = Artist Name in Title case with the second name in lower case
    Artist_name = input("Enter Artist Name : ")
    # User_Input = Song Name in lowercase
    Song_name = input("Song name : ")

    main(Artist_name, Song_name)