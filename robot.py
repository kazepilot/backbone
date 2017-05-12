import thread
import time
import nxt


class Robot(object):

    def __init__(self):
        connection_method = nxt.Method(usb=False, bluetooth=True, fantomusb=False, fantombt=False)
        self.brick = nxt.find_one_brick(method=connection_method, debug=True)
        
        self.left_motor = nxt.motor.Motor(self.brick, nxt.motor.PORT_C)
        self.right_motor = nxt.motor.Motor(self.brick, nxt.motor.PORT_A)

        self.left_distance = nxt.sensor.Ultrasonic(self.brick, nxt.sensor.PORT_3)
        self.center_distance = nxt.sensor.Ultrasonic(self.brick, nxt.sensor.PORT_2)
        self.right_distance = nxt.sensor.Ultrasonic(self.brick, nxt.sensor.PORT_1)

        # Constants
        self.SPEED = 80
        self.DEGREES = 160
        self.MOVEMENT = 150
        self.WAIT = 0.8

<<<<<<< HEAD

    def forward(self, centimeters=1):
        distance = self.MOVEMENT
        if distance < 1:
            return
        thread.start_new_thread(self._turnmotor, (self.right_motor, self.SPEED, distance))
        thread.start_new_thread(self._turnmotor, (self.left_motor, self.SPEED, distance))
        time.sleep(0.5)

    def backward(self, centimeters=1):
        distance = self.MOVEMENT - 30
        if distance < 1:
            return
=======

    def forward(self, centimeters=1):
        distance = self.MOVEMENT
        if distance < 1:
            return
        thread.start_new_thread(self._turnmotor, (self.right_motor, self.SPEED, distance))
        thread.start_new_thread(self._turnmotor, (self.left_motor, self.SPEED, distance))
        time.sleep(0.5)

    def backward(self, centimeters=1):
        distance = self.MOVEMENT - 30
        if distance < 1:
            return
>>>>>>> b0179825d8e79cf846283a781dc08070ff4450da
        thread.start_new_thread(self._turnmotor, (self.right_motor, -self.SPEED, distance))
        thread.start_new_thread(self._turnmotor, (self.left_motor, -self.SPEED, distance))
        time.sleep(self.WAIT)

    def left(self, angle=1):
<<<<<<< HEAD
        rotation = self.DEGREES + 15
=======
        rotation = self.DEGREES + 30
>>>>>>> b0179825d8e79cf846283a781dc08070ff4450da
        if angle < 1:
            return
        thread.start_new_thread(self._turnmotor, (self.right_motor, self.SPEED, rotation))
        thread.start_new_thread(self._turnmotor, (self.left_motor, -self.SPEED, rotation))
        time.sleep(self.WAIT)

    def right(self, angle=1):
<<<<<<< HEAD
        rotation = self.DEGREES - 15
=======
        rotation = self.DEGREES
>>>>>>> b0179825d8e79cf846283a781dc08070ff4450da
        if angle < 1:
            return
        thread.start_new_thread(self._turnmotor, (self.right_motor, -self.SPEED, rotation))
        thread.start_new_thread(self._turnmotor, (self.left_motor, self.SPEED, rotation))
        time.sleep(self.WAIT)

    def distance(self):
        left = self.left_distance.get_sample()
        center = self.center_distance.get_sample()
        right = self.right_distance.get_sample()

        dist = 75.0
	dist2 = 70.0

        left = (left / dist) if left < dist else 1.0
        center = (center / dist2) if center < dist2 else 1.0
        right = (right / dist) if right < dist else 1.0

<<<<<<< HEAD
        left = (left / dist) if left < dist else 1.0
        center = (center / dist) if center < dist else 1.0
        right = (right / dist) if right < dist else 1.0
=======
        # time.sleep(self.WAIT)
>>>>>>> b0179825d8e79cf846283a781dc08070ff4450da

        return [left, center, right]

    def close(self):
        self.brick.sock.close()

    def _turnmotor(self, motor, speed, degrees):
        motor.turn(speed, degrees)


def main():
<<<<<<< HEAD
    r.left()
    r.left()
    r.left()
    r.left()
    r.forward()
    r.right()
    r.right()
    r.right()
    r.right()
    r.forward()

if __name__ == '__main__':
    r = Robot()
    main()
    main()
    main()
=======
    #r.left()
    #r.left()
    #r.left()
    #r.left()
    r.forward()
    #r.right()
    #r.right()
    #r.right()
    #r.right()
    #r.forward()


if __name__ == '__main__':
    r = Robot()
>>>>>>> b0179825d8e79cf846283a781dc08070ff4450da
    main()
    #main()
    #main()
    #main()
