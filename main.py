from csv_reader import readCSV

class MSC():
    
    def __init__(self, keys, data):
        
        for i in range(len(keys)):
            key = keys[i]
            value = data[i]
            setattr(self, key, value)
    def __str__(self):
        x = 'subscriber: ' + self.subscriber
        return str(x)

        

x = readCSV('data/msc_weekly.csv', MSC)
print(x[1])