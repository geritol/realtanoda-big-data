from csv_reader import readCSV

class Tower():
    def __init__(self, id, lat, lng):
        self.id = id
        self.lat = lat 
        self.lng = lng
        self.connected = 0
        self.range = 35
    def isMe(self, lat, lng):
        if slf.lat == lat and self.lng == lng:
            return True
        return False
    def connect(self):
        self.connected += 1
    def dissconnect(self):
        self.connected -= 1

class BaseData():
    def __init__(self, keys, data):
        
        for i in range(len(keys)):
            key = keys[i]
            value = data[i]
            setattr(self, key, value)

class MSC(BaseData):
    # dataset | subscriber | TAC type | timestamp | unix | latitude | longitude'

    
    def __str__(self):
        x = 'subscriber: ' + self.subscriber
        return str(x)

        

x = readCSV('data/msc_weekly.csv', MSC)
for i in x:
    print(i)