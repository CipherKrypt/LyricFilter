import argparse
from read_csv import read_csv
from lyric_scraper import scrape
from lyrics_checker import check_lyric


def lyricFilter(filename):
    Songs = read_csv(filename, [])
    total = len(Songs)
    count = 1
    for songs in Songs:
        artist = songs[0]
        song = songs[1]
        print(f'Checking song {count} of {total}', end = '\r')
        scrape(artist, song, 'lyrics')
        if args.list != 'None':
            wordList = args.list.lstrip('[').rstrip(']').split(',')
        else:
            wordList = None
        listing_mode = args.result
        check_lyric(name = f'{artist}- {song}', filename= 'lyrics', mode = listing_mode, explicit_words= wordList)
        count+= 1


if __name__ == "__main__":

    # Allows user to control output of the function from inside the terminal
        try:
            parser = argparse.ArgumentParser(description='Access extra features of the LyricFilter')
            parser.add_argument('-f', '--file', default = 'None', help="File name of the CSV file to parse in the format 'Artist,Song'")
            parser.add_argument('-r', '--result', default= 'a', help="""'a' - for all, prints explicit and clean songs
                                'e' - for only explicit, prints all the songs containing explicit words
                                'c' - for only clean, prints all the songs containing clean words""")
            parser.add_argument('-l', '--list', default = 'None', help="A list containing additional words to monitor for")
            args = parser.parse_args()

            lyricFilter(args.file)
        except Exception as err:
            print(f"Error: {err}")
            print('Reverting to manual mode')
            filename = input('Enter CSV file to read: ')
            try:
                lyricFilter(filename)
            except Exception as Err:
                 print(f"Error: {Err}")             