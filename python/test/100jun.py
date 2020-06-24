
class Panel :
    def __init__(self, dist, width, height) :
        self.dist = dist
        self.width = width
        self.height = height

inp = int(input())

for i in range(0, inp) : 
    dist, width, height = map(split, input)