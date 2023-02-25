import csv

streetnames: set = set()

with open('./lectures/makemore/germany.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)
    for row in reader:
        streetnames.add(row['STREET'])

with open('./lectures/makemore/part1/street-names.txt', 'w', encoding='utf-8') as write_file:
    for streetname in streetnames:
        write_file.write(streetname + '\n')
