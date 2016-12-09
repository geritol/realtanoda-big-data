from csv_reader import readCSV

class BaseData():
    def __init__(self, keys, data):
        self.keys = keys

        for i in range(len(keys)):
            key = keys[i]
            value = data[i]
            setattr(self, key, value)

class MSC(BaseData):
    
    
    def __str__(self):
        return "dataset: {}, subscriber: {}, TAC: {}, type: {}, timestamp: {}, unix: {}, latitude: {}, longitude: {}".format(
            self.dataset, self.subscriber, self.TAC, self.type, self.timestamp, self.unix, self.latitude, self.longitude
        )

        

x = readCSV('data/msc_weekly.csv', MSC)
for i in x:
    print(i.latitude, i.longitude)