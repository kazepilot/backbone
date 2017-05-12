import cv2
import numpy as np
import requests
from robot import Robot
from network import Network
from detection import Detection
from config import Config
from camera import Camera
import json
from Queue import Queue
import time


class Backbone(object):

    def __init__(self, network_weights, config_file):
        self.robot = Robot()
        self.network = Network(network_weights)
        self.config = Config(config_file)
        self.camera = Camera()
        self.pre_moves = Queue()
        self.moves_stack = Queue()
        self.conditions = self.config.get_standard_conditions()
        self.additional_conditions = []

    def move(self):
        frame = self.camera.capture()
        detections = self.get_detections(frame)
        distances = self.robot.distance()
        move = 3
<<<<<<< HEAD
=======

	print self.moves_stack.empty()

>>>>>>> b0179825d8e79cf846283a781dc08070ff4450da
        if self.moves_stack.empty():
            self.pre_moves, self.moves_stack, self.additional_conditions = self.get_moves(
                detections)

        pass_conditions = self.can_move(self.conditions, detections)
        pass_add_conditions = self.can_move(
            self.additional_conditions, detections)

        if not pass_conditions:
            return False
        if not self.pre_moves.empty():
            if distances[1] < 0.05:
                return False
            move = self.pre_moves.get(False)

<<<<<<< HEAD
        elif not self.moves_stack.empty():
            if not pass_add_conditions or distances[1] < 0.05:
                return False
=======
        if not self.moves_stack.empty():
>>>>>>> b0179825d8e79cf846283a781dc08070ff4450da
            move = self.moves_stack.get(False)

        else:
            move = self.network.move(distances)

        if move is 0:
            self.robot.left()
        elif move is 1:
            self.robot.right()
        elif move is 2:
            self.robot.forward()
<<<<<<< HEAD
        else:
            time.sleep(0.5)
=======
	else:
	    time.sleep(0.5)
>>>>>>> b0179825d8e79cf846283a781dc08070ff4450da

        return True

    def get_detections(self, frame):
        encoded = cv2.imencode('.jpg', frame)[1].tostring()
        results = requests.post(
            "http://192.168.1.101:80/cyclops", data=encoded)
        height, width = frame.shape[:2]
        data = json.loads(results.content)
        detections = []
        zones = self.config.zones()

        for detection in data['objects']:
            det = Detection(detection, height, width, zones)
            det.active = self.config.is_active(det.name)
            print det.name, det.probility
	    if det.probility > 0.3:
                detections.append(det)

<<<<<<< HEAD
        return detections

    def get_moves(self, detections):
        if detections is None or len(detections) < 1:
            return Queue(), Queue(), [] 
        signs = filter(lambda x: not x.active, detections)
	
        if len(signs) < 1:
	        return Queue(), Queue(), []
	
        sign = max(signs, key=lambda x: x.area())
        moves = self.config.get_moves(sign.name)
        conditiions = self.config.get_conditions(sign.name)

        final_moves = Queue()
        distance = int(round(sign.distance())) / 6
        for i in range(0, distance):
            final_moves.put(2)

        return final_moves, moves, conditiions

    def can_move(self, conditions, detections):
        if detections is None:
=======
	return detections

    def get_moves(self, detections):
	if detections is None or len(detections) < 1:
            return Queue(), [] 
        signs = filter(lambda x: not x.active, detections)
	
	if len(signs) < 1:
	    return Queue(), []
	
	sign = max(signs, key=lambda x: x.area())
        moves = self.config.get_moves(sign.name)
        conditiions = self.config.get_conditions(sign.name)

	final_moves = Queue()
	distance = int(round(sign.distance())) / 6
	for i in range(0, distance):
	    final_moves.put(2)
	while not moves.empty():
	    final_moves.put(moves.get())

        return final_moves, conditiions

    def can_move(self, conditions, detections):
	if detections is None:
>>>>>>> b0179825d8e79cf846283a781dc08070ff4450da
            return True

        for condition in conditions:
            for detection in detections:
                if detection.active:
                    if detection.zone == condition:
                        return False

        return True

    def close(self):
        self.robot.close()


def main():
<<<<<<< HEAD
    backbone = Backbone('/home/pi/backbone/data.weights', '/home/pi/backbone/config.json')
    while 'pigs' != 'fly':
        backbone.move()
=======
    backbone = Backbone('data.weights', 'config.json')
    camera = Camera()
    while 'pigs' != 'fly':
        frame = camera.capture()
        backbone.move(frame)
>>>>>>> b0179825d8e79cf846283a781dc08070ff4450da
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()
