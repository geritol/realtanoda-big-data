import csv


def readCSV(file, dest):
    
    with open(file, "rt", encoding='utf8') as f:
        counter = 0
        reader = csv.reader(f)
        for row in reader:
            counter += 1
            with open(dest, "a", encoding='utf8') as d:
                d.write(row[0] + '\n')
            if counter > 500000:
                return
readCSV('random_felmill.csv', 'random_felmill_.csv')
