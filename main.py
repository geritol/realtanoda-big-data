from csv_reader import readCSV

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


msc_data = readCSV('data/msc_weekly.csv', MSC)

towers = []

# tower id counter
id = 0
for tower_data in msc_data:
    if towers:
        found = False
        for tower in towers:
            if tower.isMe(tower_data.latitude, tower_data.longitude):
                found = True
                break
        if not found:
            towers.append(Tower(id, tower_data.latitude, tower_data.longitude))
            id += 1
    else:
        towers.append(Tower(id, tower_data.latitude, tower_data.longitude))


# for k in towers:
#     print(k)
print(len(towers))
