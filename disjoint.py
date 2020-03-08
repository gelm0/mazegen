#Algorithms taken from https://en.wikipedia.org/wiki/Disjoint-set_data_structure
class disjoint_set():
    def __init__(self, data):
        self.parent = {}
        for obj in data:
            self.parent[obj] = obj

    def find(self, data):
        if self.parent[data] == data:
            return data
        else:
            return self.find(self.parent[data])

    def union(self, data1, data2):
        x = self.find(data1)
        y = self.find(data2)
        self.parent[x] = y
