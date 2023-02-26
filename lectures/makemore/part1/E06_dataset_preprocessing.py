import csv

streetnames = set()

UNWANTED_CHARS = ['.', '1', '2', '3', '4',
                  '5', '6', '7', '8', '9', '0', '+', ',', '\"', '_', '`', '/', ':']

REPLACABLE_CHARS = {'á': 'a', 'â': 'a', 'è': 'e',
                    'é': 'e', 'ë': 'e', 'í': 'i', 'ó': 'o'}

with open('./lectures/makemore/germany.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)
    for row in reader:
        streetname = row['STREET'].lower()
        if streetname in streetnames:
            continue
        if any(char in streetname for char in UNWANTED_CHARS):
            continue
        for char in REPLACABLE_CHARS:
            streetname = streetname.replace(char, REPLACABLE_CHARS[char])
        # remove brackets and everything inside from streetname
        if '(' in streetname:
            streetname = streetname[:streetname.index('(')]
        streetnames.add(streetname)

with open('./lectures/makemore/part1/street-names.txt', 'w', encoding='utf-8') as write_file:
    for streetname in streetnames:
        write_file.write(streetname + '\n')

print(f'Done!, wrote {len(streetnames)} street names to file.')
