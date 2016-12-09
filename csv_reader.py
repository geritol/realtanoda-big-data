import csv


def readCSV(file, className):
    
    with open(file, "rt", encoding='utf8') as f:
        header = []
        out = []
        reader = csv.reader(f)
        for row in reader:
            if(len(header) == 0):
                header = row[0].split(';')
            else:
                c = className(header, row[0].split(';'))
                out.append(c)
    return out

