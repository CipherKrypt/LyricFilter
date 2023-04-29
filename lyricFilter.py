import argparse
from read_csv import read_csv
import lyric_scraper

def lyricFilter(filename):
    Songs = read_csv(filename, [])
    for songs in Songs:
        artist = songs[0]
        song = songs[1]
        lyric_scraper.main(artist, song)
        if args.list != 'None':
            wordList = args.list.lstrip('[').rstrip(']').split(',')
        else:
            wordList = None
        listing_mode = args.result
        if  listing_mode == 'e':
            mode = 'Only Explicit'
            pass
        elif listing_mode == 'c':
            mode = 'Only Clean'
            pass
        else:
            mode = 'All'
            pass
        print(f'{artist} {song} - Mode: {mode} with WordList: {wordList}')


if __name__ == "__main__":

    # Allows user to control output of the function from inside the terminal
    parser = argparse.ArgumentParser(description='Access extra features of the LyricFilter')
    parser.add_argument('-f', '--file', default = 'None', help="File name of the CSV file to parse in the format 'Artist,Song'")
    parser.add_argument('-r', '--result', default= 'a', help="""'a' - for all, prints explicit and clean songs
                        'e' - for only explicit, prints all the songs containing explicit words
                        'c' - for only clean, prints all the songs containing clean words""")
    parser.add_argument('-l', '--list', default = 'None', help="A list containing additional words to monitor for")
    args = parser.parse_args()

    lyricFilter(args.file)