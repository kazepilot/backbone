class Detection(object):

    def __init__(self, json_data, height, width, zones, active=False, side=20):
        self.left = int(json_data['left'] * height)
        self.right = int(json_data['right'] * height)
        self.top = int(json_data['top'] * width)
        self.bottom = int(json_data['bottom'] * width)
        self.name = json_data['name']
        self.active = active

        self.zone = zones['ACTIVE']

        if self.center()[0] > width / 2:
            side = width * 15 / 100
            if self.right < side:
                self.in_active_zone = zones['LEFT']
        else:
            side = width - width * 15 / 100
            if self.left > side:
                self.in_active_zone = zones['RIGHT']

    def topD(self):
        return (self.top, self.left)

    def bottomD(self):
        return (self.bottom, self.right)

    def width(self):
        return self.right - self.left

    def height(self):
        return self.bottom - self.top

    def area(self):
        return self.height() * self.width()

    def distance(self):
        if not self.active:
            return None
        # object that has size of 100px*100px is 5cm away. Using this info we
        # can estimate how far this object is
        return 100000 / self.area() * 5

    def center(self):
        return (self.bottom - self.top, self.right - self.left)
