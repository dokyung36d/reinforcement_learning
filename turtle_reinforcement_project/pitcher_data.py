import csv

pitcher_file_path =  "rl1126wont.csv"

all_pitcher_data = []

with open(pitcher_file_path, 'r', encoding="UTF-8") as file:
    csv_reader = csv.reader(file)
    i = 0
    for row in csv_reader:
        if i == 0:
            i += 1
            row[0] = row[0][-4:]
        for j in range(5):
            row[j] = float(row[j])
        # Each 'row' variable contains a list of values from a row in the CSV file
        all_pitcher_data.append(row)

