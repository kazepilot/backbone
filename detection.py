class Detection(object):

    def __init__(self, json_data, height, width, zones, active=False, side=20):
        self.left = int(json_data['left'] * height)
        self.right = int(json_data['right'] * height)
        self.top = int(json_data['top'] * width)
        self.bottom = int(json_data['bottom'] * width)
        self.name = json_data['name']
        self.active = active
        self.probility = json_data['probability']

        self.zone = zones['CENTER']

        center = [self.bottom - self.top, self.right - self.left]

        if center[0] > width / 2:
            side = width * 15 / 100
            if self.right < side:
                self.in_active_zone = zones['LEFT']
        else:
            side = width - width * 15 / 100
            if self.left > side:
                self.in_active_zone = zones['RIGHT']

    def area(self):
        return (self.bottom - self.top) * (self.right - self.left)

    def distance(self):
        if self.active:
            return None

        distance = self.area() / -1000.0 + 50
        return distance


def main():
    from camera import Camera
    from backbone import Backbone

    cam = Camera()
    bone = Backbone('data.weights', 'config.json')

    while 'pigs' != 'fly':
        frame = cam.capture()
        detections = bone.get_detections(frame)
        for detection in detections:
            print detection.name, detection.distance()

if __name__ == '__main__':
    main()
