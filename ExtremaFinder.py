class Point(object):

    __slots__ = ('x', 'y')

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return str((self.x, self.y))

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __idiv__(self, number):
        self.x /= number
        self.y /= number
        return self

    def abs(self):
        return abs(self.x) + abs(self.y)

    def copy(self):
        return Point(self.x, self.y)


def extrema(moves, jitter=0.1, threshold=1000, sample=16):
    point = Point()
    minpoint = Point()
    maxpoint = Point()
    average = Point()
    average /= 1.0
    turned = False
    for move in moves:
        point += move
        x = point.x
        if x < minpoint.x:
            minpoint.x = x
        elif x > maxpoint.x:
            maxpoint.x = x
        y = point.y
        if y < minpoint.y:
            minpoint.y = y
        elif y > maxpoint.y:
            maxpoint.y = y
        delta = move.copy()
        delta -= average
        delta /= sample
        average += delta
        if average.abs() < jitter:
            if point.abs() > threshold:
                turned = True
            elif turned:
                yield minpoint, maxpoint
                point = Point() # reset (calibrate)
                minpoint = Point()
                maxpoint = Point()
                turned = False


# read data from file
moves = [Point(*map(int, move.split(',')))
    for move in open('data.txt').read().split(';') if move]

# generate extrema
print list(extrema(moves))