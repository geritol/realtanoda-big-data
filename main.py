import os
import pylab as plt
import math
import csv
import time
import random


from csv_reader import readCSV
from gen_random_pos import randomCoords
#from approximate_tower_ranges import gen

class Towers():
    def __init__(self):
        self.towers = []
        self.map = {}
        self.connectedStats = []

    def init(self, data, force = False):
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
            self.map[str(lat)+str(lng)] = id
            return True
            
        found = self.find(str(lat)+str(lng))

        if not found:
            self.towers.append(Tower(id, lat, lng))
            self.map[str(lat)+str(lng)] = id
    def find(self,latlngstr):
        try:
            return self.map[latlngstr]
        except KeyError:
            return False
    def num(self):
        print(len(self.towers))
    def save(self):
        file_name = 'towers.csv'
        if os.path.isfile(file_name): os.remove(file_name)
            
        with open(file_name, "w", encoding='utf8') as f:
            for i in range(len(self.towers)):
                tower = self.towers[i]
                if i == 0: f.write('id; lat; lng; bounds; distances \n')
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
    def getConnected(self):
        res = []
        for tower in self.towers:
            res.append(tower.connected)
        self.connectedStats.append(res)

    def simulate(self):
        self.time = 0
        header = []
        with open('data/msc_100k_sorted.csv', "rt", encoding='utf8') as f:
            reader = csv.reader(f)

            for line in reader:
                if header:
                    
                    data = line[0].split(';')
     
                    if self.time == 0:
                        self.time = int(data[3])
                    if self.time == data[3]:
                        key = str(data[4]) + str(data[5])

                        towerID =  self.find(key)
                        tower = self.towers[towerID]
                        #connect to tower for 2 mins

                        # call object: start_time, call_lenght, position
                        current_call = Call(int(data[3]), random.randint(1, 600), tower.getCoords())
                        tower.addCall(current_call)
                        tower.connect(2)
                        print("connected: {}, call list len: {}".format(tower.connected, len(tower.calls)))
                        break
                    else:
                        self.time += 1
                else:
                    header = line[0].split(';')
                    break

class Tower():
    def __init__(self, id, lat, lng, bounds = [], distances = []):
        self.id = id
        self.lat = float(lat)
        self.lng = float(lng)
        self.connected = 0
        self.range = 35
        self.bounds = bounds
        self.distances = distances
        self.calls = []

    def addCall(self, call):
        self.calls.append(call)

    def isMe(self, lat, lng):
        if self.lat == float(lat) and self.lng == float(lng):
            return True
        return False

    def getRange(self):
        return self.range

    def getCoords(self):
        return [self.lat, self.lng]

    def getDistance(self, lng2, latt2):
        lon1, lat1, lon2, lat2 = map(math.radians, [self.lng, self.lat, float(lng2), float(latt2)])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        km = 6367 * c
        return km
    
    def addBound(self, bound):
        self.bounds.append(bound)
        self.distances.append(self.getDistance(*bound))

    def connect(self, mins):
        self.connected += 1
        #mins
        time.sleep(mins)
        self.dissconnect()

    def dissconnect(self):
        self.connected -= 1

    def __str__(self):
        return 'id: ' + str(self.id) + ' lat: ' + str(self.lat) + ' lng: ' + str(self.lng)

    def csv(self):
        return str(self.id) + ';' + str(self.lat) + ';' + str(self.lng) + ';' + str(self.bounds) + ';' + str(self.distances) + '\n'

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
    def __init__(self, start_time, call_lenght, position):
        self.start_time = start_time
        self.call_length = call_lenght
        self.position = position
        self.end_time = start_time + call_lenght

    def isInCall(self, time):
        if time in list(range(self.start_time + self.call_length)):
            return True
        return False



    def __srt__(self):
        return 'Positon: ' + str(self.position) + ' Time: ' + str(self.start_time) + ' Lenght: ' + str(self.call_length)

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
print(towers.towers[2040].getDistance(towers.towers[2040].lat, towers.towers[2040].lng))
towers.num()
towers.simulate()
print(towers.connectedStats)
#towers.draw()

#
#with open('random_felmill_.csv', "rt", encoding='utf8') as f:
#    
#   
#    reader = csv.reader(f)
#        
#        
#
#    for line in reader:
#        distance = 2000
#        cordinates = [] 
#        t = None
#        for tower in towers.towers:
#
#            
#            #print(len(line[0].split(';')))
#            if(len(line[0].split(';')) == 2):
#                cords = line[0].split(';')
#                #print(cords)
#                dist = tower.getDistance(*cords)
#                #print(dist)
#                if dist < distance:
#                    #print(cords)
#                    distance = dist
#                    cordinates = cords
#                    t = tower
#
#        if cordinates:
#            t.addBound(cordinates)
#            #print(t.bounds)
#            #print(t.id)
                

towers.save()

