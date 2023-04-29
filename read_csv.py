import csv

def read_csv(file_name, output_list :list = None):
    # Open the CSV file in read mode
    with open(f'{file_name}.csv', 'r') as file:

        # Create a csv reader object
        reader = csv.reader(file)

        # Read the first row of the CSV file
        header = next(reader)

        # Iterate over each row in the CSV file
        for row in reader:
            # Get the first column value, the Artist name
            Artist_name = row[0]

            # Get the second column value, the Song name
            Song_name = row[1]

            if output_list != None:
                output_list.append((Artist_name, Song_name))

        if output_list != None:
            return output_list

if __name__ == "__main__":
    file_name = input("Enter file name: ")
    print(read_csv(file_name, []))
