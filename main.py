from csv_reader import readCSV

class BaseData():
    def __init__(self, keys, data):
        
        for i in range(len(keys)):
            key = keys[i]
            value = data[i]
            setattr(self, key, value)

class MSC(BaseData):
    
    
    def __str__(self):
        x = 'subscriber: ' + self.subscriber
        return str(x)

        

x = readCSV('data/msc_weekly.csv', MSC)
print(x[1])