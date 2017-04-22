import thread
import time
import nxt


class Robot(object):

    def __init__(self):
        connection_method = nxt.Method(
            usb=False, bluetooth=True, fantomusb=False, fantombt=False)
        self.brick = nxt.find_one_brick(method=connection_method)

        self.left_motor = nxt.motor.Motor(self.brick, nxt.motor.PORT_C)
        self.right_motor = nxt.motor.Motor(self.brick, nxt.motor.PORT_A)

        self.left_distance = nxt.sensor.Ultrasonic(
            self.brick, nxt.sensor.PORT_4)
        self.center_distance = nxt.sensor.Ultrasonic(
            self.brick, nxt.sensor.PORT_1)
        self.right_distance = nxt.sensor.Ultrasonic(
            self.brick, nxt.sensor.PORT_3)

        # Constants
        self.SPEED = 80
        self.DEGREES = 160
        self.MOVEMENT = 200
        self.WAIT = 0.8

    def forward(self):
        pre_distances = self.distance()

        thread.start_new_thread(
            self._turnmotor, (self.right_motor, self.SPEED, self.MOVEMENT))
        thread.start_new_thread(
            self._turnmotor, (self.left_motor, self.SPEED, self.MOVEMENT))
        time.sleep(self.WAIT)

        post_distances = self.distance()

        diff_left = pre_distances[0] - post_distances[0]
        diff_right = pre_distances[2] - post_distances[2]

        abs_left = abs(diff_left)
        abs_right = abs(diff_right)

        maximum_diff = 0.15

        # Just in case we are in strange position (i.e. 45 degrees)
        if abs_left > maximum_diff or abs_right > maximum_diff:
            return

        # everything as expected
        if abs_left == 0 and abs_right == 0:
            return

        # in case we are close
        if abs(abs_left - abs_right) < 0.05:
            return

        if abs_left > abs_right:
            thread.start_new_thread(
                self._turnmotor, (self.left_motor, self.SPEED / 2, int(diff_left * 8)))
        else:
            thread.start_new_thread(
                self._turnmotor, (self.right_motor, self.SPEED / 2, int(diff_right * 8)))

        time.sleep(self.WAIT / 2)

    def backward(self):
        thread.start_new_thread(
            self._turnmotor, (self.right_motor, -self.SPEED, self.MOVEMENT))
        thread.start_new_thread(
            self._turnmotor, (self.left_motor, -self.SPEED, self.MOVEMENT))
        time.sleep(self.WAIT)

    def left(self):
        thread.start_new_thread(
            self._turnmotor, (self.right_motor, self.SPEED, self.DEGREES))
        thread.start_new_thread(
            self._turnmotor, (self.left_motor, -self.SPEED, self.DEGREES))
        time.sleep(self.WAIT)

    def right(self):
        thread.start_new_thread(
            self._turnmotor, (self.right_motor, -self.SPEED, self.DEGREES))
        thread.start_new_thread(
            self._turnmotor, (self.left_motor, self.SPEED, self.DEGREES))
        time.sleep(self.WAIT)

    def distance(self):
        left = self.left_distance.get_sample()
        center = self.center_distance.get_sample()
        right = self.right_distance.get_sample()

        dist = 75.0

        left = (1.0 - left / dist) if left < dist else 0.0
        center = (1.0 - center / dist) if center < dist else 0.0
        right = (1.0 - right / dist) if right < dist else 0.0

        return (left, center, right)

    def close(self):
        self.brick.sock.close()

    def _turnmotor(self, motor, speed, degrees):
        motor.turn(speed, degrees)


def main():
    robot = Robot()
    robot.forward()
    robot.backward()
    robot.left()
    robot.left()
    robot.right()
    robot.right()
    robot.right()
    robot.right()
    robot.left()
    robot.left()
    print robot.distance()
    print robot.distance()
    print robot.distance()
    robot.close()

if __name__ == "__main__":
    main()
