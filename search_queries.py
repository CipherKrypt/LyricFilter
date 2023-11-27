import webbrowser

def search_queries(filename):
    with open(filename, 'r') as file:
        queries = file.read().split('\n')
        for query in queries:
            query = query.strip()
            if query:
                search_url = f'https://www.google.com/search?q="{query}"'
                webbrowser.open_new_tab(search_url)

search_queries('slogans.txt')  # Replace 'slogans.txt' with your text file containing slogans
