import csv


def readCSV(file):
	with open(file, "rt", encoding='utf8') as f:
		out = []
		reader = csv.reader(f)
		for row in reader:
			out.append(row[0].split(';'))
	return out



msc_weekly = readCSV('../msc_weekly.csv')
print(msc_weekly[0])
p