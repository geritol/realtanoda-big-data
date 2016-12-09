import os
from csv_reader import readCSV

class Towers():
    def __init__(self):
        self.towers = []
    def init (self, data, force = False):
        csv_exist = os.path.isfile('towers.csv')
        if force or not csv_exist:
            for i in data:
                self.add(i.latitude, i.longitude)
            return
        self.towers = readCSV('towers.csv', Tower, False)
        
    def add(self, lat, lng):
        id = len(self.towers)
        if id == 0: 
            self.towers.append(Tower(id, lat, lng))
            return True
            
        found = False
        for t in self.towers:
            if t.isMe(lat, lng):
                found = True
                break
        if not found: 
            self.towers.append(Tower(id, lat, lng))
    def num(self):
        print(len(self.towers))
    def save(self):
        file_name = 'towers.csv'
        if os.path.isfile(file_name): os.remove(file_name)
            
        with open(file_name, "w", encoding='utf8') as f:
            for i in range(len(self.towers)):
                tower = self.towers[i]
                if i == 0: f.write('id; lat; lng \n')
                f.write(tower.csv())
                


class Tower():
    def __init__(self, id, lat, lng):
        self.id = id
        self.lat = lat 
        self.lng = lng
        self.connected = 0
        self.range = 35
    def isMe(self, lat, lng):
        if self.lat == lat and self.lng == lng:
            return True
        return False
    def connect(self):
        self.connected += 1
    def dissconnect(self):
        self.connected -= 1
    def __str__(self):
        return 'id: ' + str(self.id) + ' lat: ' + self.lat + ' lng: ' + self.lng
    def csv(self):
        return str(self.id) + ';' + str(self.lat) + ';' + str(self.lng) +  '\n'

class BaseData():
    def __init__(self, keys, data):
        self.keys = keys

        for i in range(len(keys)):
            key = keys[i]
            value = data[i]
            setattr(self, key, value)

class MSC(BaseData):
    # dataset | subscriber | TAC type | timestamp | unix | latitude | longitude'

    def __str__(self):
        return "dataset: {}, subscriber: {}, TAC: {}, type: {}, timestamp: {}, unix: {}, latitude: {}, longitude: {}".format(
            self.dataset, self.subscriber, self.TAC, self.type, self.timestamp, self.unix, self.latitude, self.longitude
        )


data = readCSV('data/msc_weekly.csv', MSC)

towers = Towers()
towers.init(data)

print(towers.towers[2040])
towers.num()

towers.save()
    

