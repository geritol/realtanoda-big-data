import os
import pylab as plt
import math

from csv_reader import readCSV
from gen_random_pos import randomCoords
# from approximate_tower_ranges import gen

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
        if lat == '' or lng == '':
            return
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
    def draw(self):
        xs = []
        ys = []
        print(type(self.towers[0].getCoords()[0]))
        print(self.towers[0])
        for tower in self.towers:
            coords = tower.getCoords()

            xs.append(coords[0])
            ys.append(coords[1])

       
        gen(500)
        plt.plot(ys, xs, '.')
        plt.show()

class Tower():
    def __init__(self, id, lat, lng):
        self.id = id
        self.lat = float(lat)
        self.lng = float(lng)
        self.connected = 0
        self.range = 35


    def isMe(self, lat, lng):
        if self.lat == float(lat) and self.lng == float(lng):
            return True
        return False

    def getRange(self):
        return self.range

    def getCoords(self):
        return [self.lat, self.lng]

    def getDistance(self, lat2, lng2):
        lon1, lat1, lon2, lat2 = map(math.radians, [self.lng, self.lat, lng2, lat2])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        km = 6367 * c
        return km

    def connect(self):
        self.connected += 1

    def dissconnect(self):
        self.connected -= 1

    def __str__(self):
        return 'id: ' + str(self.id) + ' lat: ' + str(self.lat) + ' lng: ' + str(self.lng)

    def csv(self):
        return str(self.id) + ';' + str(self.lat) + ';' + str(self.lng) +  '\n'

class Customer():
    def __init__(self, id):
        self.id = id
        self.calls = []
    def initiateCall(self,time, tower):
        if self.calls:
            curr_pos = calls[-1].position
        else:
            position = randomCoords(tower.getRange(), *tower.getCoords())
        #position = 
        self.calls.append(Call(time, position, tower))

class Call():
    def __init__(self, time, position, tower):
        self.time = time
        self.tower = tower
        self.position = position
    def __srt__(self):
        return 'Positon: ' + str(position) + ' Time: ' + str(time) + ' Tower: ' + str(tower)

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

print(towers.towers[2040].getDistance(47.603111, 19.060024))
towers.num()
towers.draw()


towers.save()

