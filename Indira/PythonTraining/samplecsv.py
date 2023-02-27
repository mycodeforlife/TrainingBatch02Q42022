import csv

with open("smlsmple.csv", newline='') as input_file:
    data_content = csv.DictReader(input_file)

    for each in data_content:
        print(each)